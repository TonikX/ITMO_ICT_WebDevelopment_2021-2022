from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(response, user)
            return redirect(response.GET.get('next', '/'))
        else:
            messages.error(response, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})
