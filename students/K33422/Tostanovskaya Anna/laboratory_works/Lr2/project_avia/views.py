from django.shortcuts import render, redirect
from django.http import Http404
from project_avia.models import Flight
from project_avia.models import Company
from project_avia.models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, CommentForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
import datetime

# Create your views here.


def all_flights(request):
    context = {}
    context["dataset"] = Flight.objects.all()
    return render(request, "all_flights.html", context)


def flight_info(request, fly_id):
    context = {}
    fly = Flight.objects.get(pk=fly_id)
    context["fly"] = fly

 #   context["themes_id"] = Conference_themes.objects.filter(conference=conf_id)
    context["comments"] = Comment.objects.filter(flight_num=fly_id).order_by('date')

    form = CommentForm(request.POST)
    context['form'] = form

    if form.is_valid():
        object = form.save(commit=False)
        object.flight_num = fly
        object.person = request.user
        object.date = datetime.datetime.now()
        object.save()
        return redirect('/flight_info/'+str(fly_id))
    return render(request, "flight_info.html", context)


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/all_flights/')
    return render(request, 'register.html', {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/all_flights/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/all_flights/")