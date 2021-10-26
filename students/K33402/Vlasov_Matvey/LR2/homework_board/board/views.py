from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Length
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView, CreateView

from board.forms import *
from board.models import *


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

        tasks_total = []
        assignments_graded = []
        assignments_total = []
        average_grade = []

        if teacher is not None:
            class_disciplines = ClassDiscipline.objects.filter(teacher=teacher) \
                .order_by('discipline__name', 'class_school__name')
            for obj in class_disciplines.all():
                tasks_list = get_tasks_list(obj.class_school.pk, obj.discipline.pk)
                tasks_total.append(len(set(tasks_list)))

                assignments_graded.append(Assignment.objects.filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline=obj.discipline,
                    grade__isnull=False))

                # Here we select assignments by pk to avoid repetition
                assignments_total.append(Assignment.objects.values('task__pk').filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline=obj.discipline))
            context['tasks_total'] = tasks_total
        else:
            class_disciplines = ClassDiscipline.objects.filter(class_school=student.class_school) \
                .order_by('discipline__name')
            for obj in class_disciplines.all():
                assignments_graded.append(Assignment.objects.filter(
                    student__user=user, task__discipline=obj.discipline, grade__isnull=False))
                assignments_total.append(Assignment.objects.filter(
                    student__user=user, task__discipline=obj.discipline))

        for obj in assignments_graded:
            grades = list(map(lambda x: x.grade, obj.all()))
            if len(grades) == 0:
                average_grade.append(None)
                continue
            avg_grade = sum(grades) / len(grades)
            avg_grade = float("{:.2f}".format(avg_grade))
            average_grade.append(avg_grade)

        context['class_disciplines'] = class_disciplines
        context['assignments_graded'] = list(map(lambda x: len(x), assignments_graded))
        context['assignments_total'] = list(map(lambda x: len(x), assignments_total))
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
        student_argument = kwargs.get('student', None)

        if teacher is not None and student_argument is None:
            context = get_teacher_discipline_tasks(class_school, discipline, context)
        else:
            student_pk = student.pk if student is not None else student_argument
            context['assignments'] = Assignment.objects.filter(student__pk=student_pk, task__discipline__pk=discipline.pk) \
                .order_by('grade', 0 ** 0 ** Length('solution'), 'deadline', '-last_submission')

        context['student_argument'] = Student.objects.get(pk=student_argument) if student_argument is not None else None
        context['discipline'] = discipline
        context['class'] = class_school
        return render(request, 'board/discipline_detail.html', context)


def get_teacher_discipline_tasks(class_school, discipline, context):  # for discipline_detail
    tasks_list = get_tasks_list(class_school.pk, discipline.pk)
    tasks = Task.objects.filter(pk__in=tasks_list)

    assignments = Assignment.objects.all()

    assignments_total = []
    assignments_graded = []
    average_grade = []
    class_list = []

    for task in sorted(set(tasks_list)):
        assignments_total.append(assignments.filter(
            student__class_school__pk=class_school.pk, task__discipline=discipline,
            task__pk=task))
        assignments_graded.append(assignments.filter(
            student__class_school__pk=class_school.pk, task__discipline=discipline,
            task__pk=task, grade__isnull=False))
        class_list.append(class_school)

    for obj in assignments_graded:
        grades = list(map(lambda x: x.grade, obj.all()))
        if len(grades) == 0:
            average_grade.append(None)
            continue
        avg_grade = sum(grades) / len(grades)
        avg_grade = float("{:.2f}".format(avg_grade))
        average_grade.append(avg_grade)

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
        if type(value) == list or type(value) == int:
            dictionary[key] += value
        else:
            dictionary[key] |= value
    return dictionary


def get_tasks_list(class_school, discipline):
    tasks_list = Assignment.objects.values('task__pk').filter(
        student__class_school__pk=class_school, task__discipline__pk=discipline)
    tasks_list = list(map(lambda x: x['task__pk'], tasks_list))
    return tasks_list


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
        return reverse('discipline_list')


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'student': student, 'tasks': None}

        if student is None:
            return render(request, 'board/task_list.html', context)
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
        teacher = None
        try:
            teacher = ClassDiscipline.objects.filter(class_school=class_school.pk, discipline=task.discipline.pk) \
                .first().teacher
        except AttributeError:
            pass

        context = {'task': task, 'class': class_school, 'teacher': teacher}

        if teacher is not None:
            assignments = Assignment.objects.filter(task__pk=task.pk, student__class_school=class_school) \
                .order_by('student__user__last_name', 'student__user__first_name', 'grade', 'deadline')
            context['assignments'] = assignments

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

        tasks = Task.objects.all().order_by('discipline__name')
        context['tasks'] = tasks
        class_disciplines = ClassDiscipline.objects.filter(teacher=teacher.pk)
        disciplines = set(map(lambda x: x.discipline.pk, class_disciplines))
        context['disciplines'] = disciplines
        request_filters = str(request).split('/')[-2]
        context['filter_by'] = request_filters

        return render(request, 'board/task_available_list.html', context)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Task
    template_name = 'board/task_delete_form.html'

    def get_success_url(self):
        return reverse('task_available_list')


class AssignmentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'

    model = Assignment
    form_class = AssignmentCreateForm
    template_name = "board/assignment_create_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['class'] = self.kwargs.get('class', None)
        kwargs['student'] = self.kwargs.get('student', None)
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        valid = True
        print(valid)
        print(valid)

        if timezone.now() > obj.deadline:
            form.add_error("deadline", "Deadline cannot be earlier than now")
            valid = False

        class_school = form.data.get('class_school', None)

        if class_school == '-1':
            form.add_error("class_school", f"Select class")
            valid = False
        elif class_school is not None and valid:
            class_school = int(class_school)
            students = Student.objects.filter(class_school__pk=class_school)
            student_teacher = ClassDiscipline.objects.filter(discipline=obj.task.discipline.pk,
                                                             class_school=class_school).first()
            if student_teacher is None or student_teacher.teacher.user.pk != self.request.user.pk:
                form.add_error("class_school", f"You are not {obj.task.discipline} teacher for this class")
                valid = False
            else:
                for student in students:
                    Assignment.objects.create(task=obj.task, deadline=obj.deadline, student=student)
                return HttpResponseRedirect(self.get_success_url())

        elif class_school is None:
            student_teacher = ClassDiscipline.objects.filter(discipline=obj.task.discipline.pk,
                                                             class_school=obj.student.class_school.pk).first()
            if student_teacher is None or student_teacher.teacher.user.pk != self.request.user.pk:
                form.add_error("student", f"You are not {obj.task.discipline} teacher for this student")
                valid = False

        if not valid:
            return render(self.request, 'board/assignment_create_form.html', {'form': form})

        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('discipline_list')


class ClassDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        class_school = Class.objects.get(pk=kwargs['pk'])
        discipline = Discipline.objects.get(pk=kwargs['discipline'])
        teacher = None
        try:
            teacher = ClassDiscipline.objects.filter(class_school=class_school.pk, discipline=discipline.pk) \
                .first().teacher
        except AttributeError:
            pass

        context = {'class': class_school, 'discipline': discipline, 'teacher': teacher}

        if teacher is not None:
            assignments = Assignment.objects.values('student__pk', 'student__user__last_name',
                                                    'student__user__first_name', 'grade') \
                .filter(student__class_school__pk=class_school.pk, task__discipline__pk=discipline.pk) \
                .order_by('student__user__last_name', 'student__user__first_name')

            all_students = Student.objects.filter(class_school=class_school.pk).order_by(
                'user__last_name', 'user__first_name')
            all_students_ids = list(map(lambda x: x.pk, all_students))
            students = {}
            last_student = -1
            i = -1
            for obj in assignments:
                student_id = obj['student__pk']

                if last_student != student_id:
                    i += 1
                    while student_id != all_students_ids[i]:
                        student = all_students.filter(pk=all_students_ids[i]).first()
                        students[all_students_ids[i]] = \
                            {'name': f"{student.user.first_name} {student.user.last_name}",
                             'grades': [], 'assignments_total': 0, 'assignments_graded': 0,
                             'average_grade': None}
                        i += 1

                last_student = student_id

                if student_id not in students.keys():
                    students[student_id] = \
                        {'name': f"{obj['student__user__last_name']} {obj['student__user__first_name']}",
                         'grades': [obj['grade']], 'assignments_total': 0, 'assignments_graded': 0,
                         'average_grade': None}
                else:
                    students[student_id]['grades'].append(obj['grade'])
            print(students)
            for key in students.keys():
                grades = list(filter(lambda x: x is not None, students[key]['grades']))
                students[key]['assignments_total'] = len(students[key]['grades'])
                students[key]['assignments_graded'] = len(grades)
                students[key]['grades'] = ', '.join(str(g) for g in grades)

                if len(grades) == 0:
                    continue
                avg_grade = sum(grades) / len(grades)
                avg_grade = float("{:.2f}".format(avg_grade))
                students[key]['average_grade'] = avg_grade

            context['students'] = students.values()
            context['ids'] = list(students.keys())
        return render(request, 'board/class_detail.html', context)
