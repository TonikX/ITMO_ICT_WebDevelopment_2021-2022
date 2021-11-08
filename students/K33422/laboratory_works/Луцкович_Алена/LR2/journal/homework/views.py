from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import *


class Homepage(TemplateView):
    template_name = "index.html"


def register(request):
    if request.user.is_authenticated:
        return redirect('/tasks/')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')

        data = {'form': form}
        return render(request, 'register.html', data)


def login_(request):
    if request.user.is_authenticated:
        return redirect('/tasks/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/tasks/')

        data = {}
        return render(request, 'login.html', data)


def logout_(request):
    logout(request)
    return redirect('login')


class ListTasks(ListView):
    model = Task
    template_name = 'list_tasks.html'

    def get_queryset(self):
        return Task.objects.all()


class Assignment(DetailView):
    model = Task
    template_name = "assignment.html"


class FinishedTasks(ListView):
    model = Entry
    template_name = 'finished_tasks.html'

    def get_queryset(self):
        return Entry.objects.all()


class AddEntry(CreateView):
    form_class = AddEntryForm
    model = Entry
    template_name = 'add_entry.html'


class UpdateEntry(UpdateView):
    model = Entry
    fields = ['submission']
    template_name = 'update_entry.html'


class DeleteEntry(DeleteView):
    model = Entry
    template_name = 'delete_entry.html'


class Grades(ListView):
    model = Entry
    template_name = 'grades.html'

    def get_queryset(self):
        return Entry.objects.all()
