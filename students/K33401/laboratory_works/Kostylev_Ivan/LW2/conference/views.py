from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from conference.forms import ReviewForm, RegistrationForm
from conference.models import Conference, User


class ConferenceList(ListView):
    model = Conference
    template_name = 'conf/conferences.html'


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "conf/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "conf/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "conf/register.html")


@login_required
def review(request):
    context = {}
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.user = request.user
        try:
            data.save()
            form = ReviewForm()  # clean the form
        except IntegrityError:
            messages.error(request, "You can't submit task again")
    context['form'] = form
    return render(request, "conf/review.html", context)


@login_required
def registration_to_conf(request):
    context = {}
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        try:
            data.save()
            form = RegistrationForm()
        except IntegrityError:
            messages.error(request, "You can't submit task again")
    context['form'] = form
    return render(request, "conf/registration_to_conf.html", context)
