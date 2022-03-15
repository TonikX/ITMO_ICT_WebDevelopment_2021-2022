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


def get_teacher_student(user, context=None):
    if context is None:
        context = {}

    teacher = Teacher.objects.all().filter(pk=user.pk).first()
    student = Student.objects.all().filter(pk=user.pk).first()
    context['teacher'] = teacher
    context['student'] = student
    return teacher, student, context


def get_task_list(class_school, discipline):
    task_list = Assignment.objects.values('task__pk').filter(
        student__class_school__pk=class_school, task__discipline__pk=discipline)
    task_list = list(map(lambda x: x['task__pk'], task_list))
    return task_list


def get_average_grades(assignments_graded):
    average_grades = []
    for obj in assignments_graded:
        grades = list(map(lambda x: x.grade, obj.all()))
        if len(grades) == 0:
            average_grades.append(None)
            continue
        avg_grade = sum(grades) / len(grades)
        avg_grade = float("{:.2f}".format(avg_grade))
        average_grades.append(avg_grade)

    return average_grades


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher, student, context = get_teacher_student(user)
        return render(request, 'board/home.html', context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher, student, context = get_teacher_student(user)
        return render(request, 'board/profile.html', context)


class DisciplineListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher, student, context = get_teacher_student(user)
        context['class_disciplines'] = None

        if teacher is None and student is None:
            return render(request, 'board/discipline_list.html', context)

        tasks_total = []
        assignments_graded = []
        assignments_total = []

        if teacher is not None:
            class_disciplines = ClassDiscipline.objects.filter(teacher=teacher) \
                .order_by('discipline__name', Length('class_school__name'), 'class_school__name')
            for obj in class_disciplines.all():
                task_list = get_task_list(obj.class_school.pk, obj.discipline.pk)
                tasks_total.append(len(set(task_list)))
                context['tasks_total'] = tasks_total

                assignments_graded.append(Assignment.objects.filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline__pk=obj.discipline.pk,
                    grade__isnull=False))
                assignments_total.append(Assignment.objects.filter(
                    student__class_school__pk=obj.class_school.pk, task__discipline__pk=obj.discipline.pk))
        else:
            class_disciplines = ClassDiscipline.objects.filter(class_school__pk=student.class_school.pk) \
                .order_by('discipline__name')
            for obj in class_disciplines.all():
                assignments_graded.append(Assignment.objects.filter(
                    student__user__pk=user.pk, task__discipline__pk=obj.discipline.pk, grade__isnull=False))
                assignments_total.append(Assignment.objects.filter(
                    student__user__pk=user.pk, task__discipline__pk=obj.discipline.pk))

        context['class_disciplines'] = class_disciplines
        context['assignments_graded'] = list(map(lambda x: len(x), assignments_graded))
        context['assignments_total'] = list(map(lambda x: len(x), assignments_total))
        context['average_grade'] = get_average_grades(assignments_graded)

        return render(request, 'board/discipline_list.html', context)


class DisciplineDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher, student, context = get_teacher_student(user)
        context['tasks'] = None

        if teacher is None and student is None:
            return render(request, 'board/discipline_detail.html', context)

        discipline = Discipline.objects.get(pk=kwargs['pk'])
        class_school = Class.objects.get(pk=kwargs['class'])
        student_argument = kwargs.get('student', None)

        if teacher is not None and student_argument is None:
            context = get_discipline_teacher_tasks(class_school, discipline, context)
        else:
            student_pk = student.pk if student is not None else student_argument
            # order by grade_comment/solution length to check whether task commented/submitted
            context['assignments'] = Assignment.objects.filter(student__pk=student_pk, task__discipline__pk=discipline.pk) \
                .order_by('grade', 0 ** 0 ** Length('grade_comment'), 0 ** 0 ** Length('solution'), 'deadline', '-last_changed')

        context['student_argument'] = Student.objects.get(pk=student_argument) if student_argument is not None else None
        context['discipline'] = discipline
        context['class'] = class_school
        return render(request, 'board/discipline_detail.html', context)


def get_discipline_teacher_tasks(class_school, discipline, context):
    task_list = get_task_list(class_school.pk, discipline.pk)
    tasks = Task.objects.filter(pk__in=task_list)

    assignments_total = []
    assignments_graded = []
    class_list = []

    for task in sorted(set(task_list)):
        assignments_total.append(Assignment.objects.filter(
            student__class_school__pk=class_school.pk, task__discipline__pk=discipline.pk,
            task__pk=task))
        assignments_graded.append(Assignment.objects.filter(
            student__class_school__pk=class_school.pk, task__discipline=discipline.pk,
            task__pk=task, grade__isnull=False))
        class_list.append(class_school)

    context['class'] = class_list
    context['tasks'] = tasks
    context['assignments_total'] = list(map(lambda x: len(x), assignments_total))
    context['assignments_graded'] = list(map(lambda x: len(x), assignments_graded))
    context['average_grade'] = get_average_grades(assignments_graded)
    return context


class TaskAvailableListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        teacher = Teacher.objects.all().filter(pk=user.pk).first()
        context = {'teacher': teacher, 'tasks': None}

        if teacher is None:
            return render(request, 'board/task_available_list.html', context)

        tasks = Task.objects.all().order_by('discipline__name', 'title')
        context['tasks'] = tasks
        class_disciplines = ClassDiscipline.objects.filter(teacher__pk=teacher.pk)
        disciplines = set(map(lambda x: x.discipline.pk, class_disciplines))
        context['disciplines'] = disciplines
        request_filters = str(request).split('/')[-2]
        context['filter_by'] = request_filters

        return render(request, 'board/task_available_list.html', context)


class AssignmentListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        student = Student.objects.all().filter(pk=user.pk).first()
        context = {'student': student, 'tasks': None}

        if student is None:
            return render(request, 'board/assignment_list.html', context)
        else:
            # order by grade_comment/solution length to check whether task commented/submitted
            context['tasks'] = Assignment.objects.filter(student__pk=self.request.user.pk) \
                .order_by('grade', 0 ** 0 ** Length('grade_comment'), 0 ** 0 ** Length('solution'), 'deadline', '-last_changed')

        return render(request, 'board/assignment_list.html', context)


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        class_school = Class.objects.get(pk=kwargs['class'])
        teacher = None
        try:
            teacher = ClassDiscipline.objects.filter(class_school__pk=class_school.pk, discipline__pk=task.discipline.pk) \
                .first().teacher
        except AttributeError:
            pass

        context = {'task': task, 'class': class_school, 'teacher': teacher}

        if teacher is not None:
            assignments = Assignment.objects.filter(task__pk=task.pk, student__class_school__pk=class_school.pk) \
                .order_by('student__user__last_name', 'student__user__first_name', 'grade', 'deadline')
            context['assignments'] = assignments

        return render(request, 'board/task_detail.html', context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'

    model = Task
    form_class = TaskForm
    template_name = "board/task_create_form.html"

    def form_valid(self, form):
        form.instance.author = Teacher.objects.get(user__pk=self.request.user.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_available_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Task
    form_class = TaskForm
    template_name = "board/task_update_form.html"

    def get_success_url(self):
        return reverse('task_available_list')


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
        kwargs['task'] = self.kwargs.get('task', None)
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        valid = True

        if timezone.now() > obj.deadline:
            form.add_error("deadline", "Deadline cannot be earlier than now")
            valid = False

        class_school = form.data.get('class_school', None)

        if class_school == '-1':
            form.add_error("class_school", "Select class")
            valid = False

        elif class_school is not None and valid:
            class_school = int(class_school)
            students = Student.objects.filter(class_school__pk=class_school)
            student_teacher = ClassDiscipline.objects.filter(discipline__pk=obj.task.discipline.pk,
                                                             class_school__pk=class_school).first()
            if student_teacher is None or student_teacher.teacher.user.pk != self.request.user.pk:
                form.add_error("class_school", f"You are not {obj.task.discipline} teacher for this class")
                valid = False
            else:
                for student in students:
                    Assignment.objects.create(task=obj.task, deadline=obj.deadline, student=student)
                return HttpResponseRedirect(self.get_success_url())

        elif class_school is None:
            student_teacher = ClassDiscipline.objects.filter(discipline__pk=obj.task.discipline.pk,
                                                             class_school__pk=obj.student.class_school.pk).first()
            if student_teacher is None or student_teacher.teacher.user.pk != self.request.user.pk:
                form.add_error("student", f"You are not {obj.task.discipline} teacher for this student")
                valid = False

        if not valid:
            return render(self.request, 'board/assignment_create_form.html', {'form': form})

        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('discipline_list')


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


class ClassDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        class_school = Class.objects.get(pk=kwargs['pk'])
        discipline = Discipline.objects.get(pk=kwargs['discipline'])
        teacher = None
        try:
            teacher = ClassDiscipline.objects.filter(class_school__pk=class_school.pk, discipline__pk=discipline.pk) \
                .first().teacher
        except AttributeError:
            pass

        context = {'class': class_school, 'discipline': discipline, 'teacher': teacher}

        if teacher is not None:
            assignments = Assignment.objects.values('student__pk', 'student__user__last_name',
                                                    'student__user__first_name', 'grade') \
                .filter(student__class_school__pk=class_school.pk, task__discipline__pk=discipline.pk) \
                .order_by('student__user__last_name', 'student__user__first_name')

            all_students = Student.objects.filter(class_school__pk=class_school.pk).order_by(
                'user__last_name', 'user__first_name')
            all_students_ids = list(map(lambda x: x.pk, all_students))
            students = {}

            last_student = -1
            i = 0
            for obj in assignments:
                student_id = obj['student__pk']

                if last_student != student_id:
                    # this loop is necessary to add students without assignments
                    while student_id != all_students_ids[i]:
                        student = all_students.filter(pk=all_students_ids[i]).first()
                        students[all_students_ids[i]] = \
                            {'name': f"{student.user.first_name} {student.user.last_name}",
                             'grades': [], 'assignments_total': 0, 'assignments_graded': 0,
                             'average_grade': None}
                        i += 1
                    i += 1

                last_student = student_id

                if student_id not in students.keys():
                    students[student_id] = \
                        {'name': f"{obj['student__user__last_name']} {obj['student__user__first_name']}",
                         'grades': list([obj['grade']]), 'assignments_total': 0, 'assignments_graded': 0,
                         'average_grade': None}
                else:
                    students[student_id]['grades'].append(obj['grade'])

            for student in all_students[i:]:
                students[all_students_ids[i]] = \
                    {'name': f"{student.user.first_name} {student.user.last_name}",
                     'grades': [], 'assignments_total': 0, 'assignments_graded': 0,
                     'average_grade': None}
                i += 1

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
