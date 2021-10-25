from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Length
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView, CreateView

from board.forms import AssignmentStudentForm, AssignmentGradeForm, TaskForm
from board.models import ClassDiscipline, Teacher, Student, Discipline, Assignment, Task, Class


class HomeView(TemplateView):
    template_name = 'board/home.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'student': student}
        return render(request, 'board/profile.html', context)


class DisciplineListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'student': student, 'class_disciplines': None}

        if teacher is None and student is None:
            return render(request, 'board/discipline_list.html', context)

        tasks_graded = []
        tasks_total = []
        average_grade = []

        if teacher is not None:
            class_disciplines = ClassDiscipline.objects.filter(teacher=teacher) \
                .order_by('discipline', 'class_school')
            for obj in class_disciplines.all():
                tasks_graded.append(Assignment.objects.filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline=obj.discipline,
                    grade__isnull=False))

                # Here we select tasks by pk to avoid repetition
                tasks_total.append(Assignment.objects.values('task__pk').filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline=obj.discipline))
        else:
            class_disciplines = ClassDiscipline.objects.filter(class_school=student.class_school) \
                .order_by('discipline')
            for obj in class_disciplines.all():
                tasks_graded.append(Assignment.objects.filter(
                    student__user=user, task__discipline=obj.discipline, grade__isnull=False))
                tasks_total.append(Assignment.objects.filter(
                    student__user=user, task__discipline=obj.discipline))

        for obj in tasks_graded:
            grades = list(map(lambda x: x.grade, obj.all()))
            if len(grades) == 0:
                average_grade.append(None)
                continue
            average_grade.append(sum(grades) / len(grades))

        context['class_disciplines'] = class_disciplines
        context['tasks_graded'] = list(map(lambda x: len(x), tasks_graded))
        context['tasks_total'] = list(map(lambda x: len(x), tasks_total))
        context['average_grade'] = average_grade

        return render(request, 'board/discipline_list.html', context)


class DisciplineDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'student': student, 'tasks': None}

        if teacher is None and student is None:
            return render(request, 'board/discipline_detail.html', context)

        discipline = Discipline.objects.get(pk=kwargs['pk'])
        class_school = Class.objects.get(pk=kwargs['class'])

        if teacher is not None:
            context = get_teacher_discipline_tasks(class_school, discipline, context)
        else:
            context['assignments'] = Assignment.objects.filter(student__pk=user.pk, task__discipline__pk=discipline.pk) \
                .order_by('grade', 0 ** 0 ** Length('solution'), 'deadline', '-last_submission')

        context['discipline'] = discipline
        context['class'] = class_school
        return render(request, 'board/discipline_detail.html', context)


def get_teacher_discipline_tasks(class_school, discipline, context):
    tasks_list = Assignment.objects.values('task__pk').filter(
        student__class_school__pk=class_school.pk, task__discipline=discipline)
    tasks_list = list(map(lambda x: x['task__pk'], tasks_list))
    tasks = Task.objects.filter(pk__in=tasks_list)

    assignments_total = []
    assignments_graded = []
    average_grade = []
    class_list = []
    for task in tasks_list:
        assignments_total.append(Assignment.objects.filter(
            student__class_school__pk=class_school.pk, task__discipline=discipline,
            task__pk=task))
        assignments_graded.append(Assignment.objects.filter(
            student__class_school__pk=class_school.pk, task__discipline=discipline,
            task__pk=task, grade__isnull=False))
        class_list.append(class_school)

    for obj in assignments_graded:
        grades = list(map(lambda x: x.grade, obj.all()))
        if len(grades) == 0:
            average_grade.append(None)
            continue
        average_grade.append(sum(grades) / len(grades))

    print(class_list)
    dictionary_append(context, 'class', class_list)
    dictionary_append(context, 'tasks', tasks)
    dictionary_append(context, 'assignments_total', list(map(lambda x: len(x), assignments_total)))
    dictionary_append(context, 'assignments_graded', list(map(lambda x: len(x), assignments_graded)))
    dictionary_append(context, 'average_grade', average_grade)
    return context


def dictionary_append(dictionary, key, value):
    if key not in dictionary or dictionary[key] is None:
        dictionary[key] = value
    else:
        if type(value) == list:
            dictionary[key] += value
        else:
            dictionary[key] |= value
    return dictionary


class AssignmentStudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'

    model = Assignment
    form_class = AssignmentStudentForm
    template_name = 'board/assignment_student_form.html'
    success_message = "Assignment successfully submitted"

    def get_success_url(self):
        return reverse('assignment_student_update', kwargs={'pk': self.kwargs['pk']})


class AssignmentGradeView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Assignment
    form_class = AssignmentGradeForm
    template_name = 'board/assignment_grade_form.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        assignment = Assignment.objects.get(pk=pk)
        return reverse('task', kwargs={'pk': assignment.task.pk, 'class': assignment.student.class_school.pk})


class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Assignment
    template_name = 'board/assignment_delete_form.html'

    def get_success_url(self):
        return reverse('task_list')


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'student': student, 'tasks': None}

        if teacher is None and student is None:
            return render(request, 'board/task_list.html', context)

        if teacher is not None:
            t_list = ClassDiscipline.objects.filter(teacher=teacher)
            print(t_list)
            for obj in t_list.values():
                class_school = Class.objects.get(pk=obj['class_school_id'])
                context = get_teacher_discipline_tasks(class_school, obj['discipline_id'], context)
        else:
            # order by solution length to check whether task submitted
            context['tasks'] = Assignment.objects.filter(student=self.request.user.pk) \
                .order_by('grade', 0 ** 0 ** Length('solution'), 'deadline', '-last_submission')

        return render(request, 'board/task_list.html', context)


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        class_school = Class.objects.get(pk=kwargs['class'])
        teacher = ClassDiscipline.objects.get(class_school=class_school, discipline=task.discipline)

        assignments = Assignment.objects.filter(task__pk=task.pk, student__class_school=class_school) \
            .order_by('student__user__last_name', 'student__user__first_name')
        context = {'task': task, 'class': class_school, 'teacher': teacher, 'assignments': assignments}
        return render(request, 'board/task_detail.html', context)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Task
    form_class = TaskForm
    template_name = "board/task_update_form.html"

    def get_success_url(self):
        return reverse('task_available_list')


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'

    model = Task
    form_class = TaskForm
    template_name = "board/task_create_form.html"

    def form_valid(self, form):
        form.instance.author = Teacher.objects.get(user=self.request.user.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_available_list')


class TaskAvailableListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'tasks': None}

        if teacher is None:
            return render(request, 'board/task_available_list.html', context)

        tasks = Task.objects.all().order_by('discipline')
        context['tasks'] = tasks

        return render(request, 'board/task_available_list.html', context)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Task
    template_name = 'board/task_delete_form.html'

    def get_success_url(self):
        return reverse('task_list')
