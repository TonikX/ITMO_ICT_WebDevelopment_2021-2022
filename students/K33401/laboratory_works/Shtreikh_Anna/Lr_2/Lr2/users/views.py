from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect
from requests import auth
from django.contrib.auth.models import User, auth

from hotels.models import Reservation
from .forms import *
# Create your views here.

def log(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('/login/')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})

def profile(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'profile.html', {'reservations': reservations, 'user': user})