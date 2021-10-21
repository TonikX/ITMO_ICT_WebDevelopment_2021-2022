from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from main.models import Pupil


def index(request):
    return render(request, 'main/index.html', locals())


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('room-list'))
        else:
            error_text = 'Неправильный логин или пароль'

    return render(request, 'register/login.html', locals())


def register(request):
    if request.method == "POST":
        username = request.POST['username']

        user = User.objects.filter(username=username)

        if len(user) == 0:
            pupil = Pupil.from_post(request.POST)
            login(request, pupil.user)

            return redirect(reverse_lazy('room-list'))
        else:
            error_text = 'Пользователь с таким логином уже существует'

    return render(request, 'register/register.html', locals())


def logout_view(request):
    logout(request)

    return redirect(reverse_lazy('login'))
