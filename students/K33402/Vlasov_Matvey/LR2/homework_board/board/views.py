from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import TemplateView, DetailView, ListView, UpdateView

from board.forms import SubmissionForm
from board.models import ClassDiscipline, Teacher, Student, Discipline, Submission


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
        context = {'class_disciplines': None}
        if teacher is not None:
            context['class_disciplines'] = ClassDiscipline.objects.filter(teacher=teacher)
        elif student is not None:
            class_disciplines = ClassDiscipline.objects.filter(class_school=student.class_school)
            tasks_done = []
            tasks_total = []
            average_grade = []

            for obj in class_disciplines.all():
                tasks_done.append(Submission.objects.filter(
                    student__user=user, assignment__discipline=obj.discipline, grade__isnull=False))
                tasks_total.append(Submission.objects.filter(
                    student__user=user, assignment__discipline=obj.discipline))

            for obj in tasks_done:
                grades = list(map(lambda x: x.grade, obj.all()))
                if len(grades) == 0:
                    average_grade.append(None)
                    continue
                average_grade.append(sum(grades) / len(grades))

            context['class_disciplines'] = class_disciplines
            context['tasks_done'] = list(map(lambda x: len(x), tasks_done))
            context['tasks_total'] = list(map(lambda x: len(x), tasks_total))
            context['average_grade'] = average_grade
            print(average_grade)

        return render(request, 'board/discipline_list.html', context)


class DisciplineDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        discipline = Discipline.objects.get(pk=kwargs['pk'])
        tasks = Submission.objects.filter(student=user.pk, assignment__discipline=discipline)
        context = {'discipline': discipline, 'tasks': tasks}
        return render(request, 'board/discipline_detail.html', context)


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'

    model = Submission
    form_class = SubmissionForm

    def get_success_url(self):
        return reverse('submission', kwargs={'pk': self.kwargs['pk']})

