from copy import copy

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from conference.forms import ReviewForm
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

# @login_required
# def conf_list(request):
#     confs = Conference.objects.all()
#     context = {'confs': confs}
#     return render(request, "conf/registration_to_conf.html", context)


@login_required
def registration_to_conf(request, pk):
    conf = Conference.objects.get(id=pk)

    if conf.members.filter(id=request.user.id).exists():
        conf.members.remove(request.user)
    else:
        conf.members.add(request.user)
    confs = Conference.objects.all()
    # context = {'conferences': confs}
    return redirect('regtoconf')


@login_required
def conf_for_reg(request):
    conferences = copy(Conference.objects.all())
    user_id = request.user.id
    conferences.is_registered = False
    for conference in conferences:
        conference.is_registered = conference.members.filter(id=user_id).exists()
    context = {'conferences': conferences}
    return render(request, 'conf/registration_to_conf.html', context)


def redirect_to_confs(request):
    response = redirect('/conferences/')
    return response

def members_of_conference(request):
    confs = Conference.objects.all()
    users = User.objects.all()

    context = {'confs': confs, 'users': users}
    return render(request, 'conf/members.html', context)
