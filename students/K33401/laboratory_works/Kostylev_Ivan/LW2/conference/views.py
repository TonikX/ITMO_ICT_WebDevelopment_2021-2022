from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.generic import ListView
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render

from conference.forms import ReviewForm, RegistrationForm
from conference.models import Conference


class ConferenceList(ListView):
    model = Conference
    template_name = 'conferences.html'


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
    return render(request, "review.html", context)


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
    return render(request, "registration_to_conf.html", context)
