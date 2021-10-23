from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from board.models import Discipline, Teacher, Student


class HomeView(TemplateView):
    template_name = 'board/home.html'


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        teacher = Teacher.objects.all().filter(pk=self.request.user.pk).first()
        student = Student.objects.all().filter(pk=self.request.user.pk).first()
        context = {'teacher': teacher, 'student': student}
        return render(request, 'board/profile.html', context)