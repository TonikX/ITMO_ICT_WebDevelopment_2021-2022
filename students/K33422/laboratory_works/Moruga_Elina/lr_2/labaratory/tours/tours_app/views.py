from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Users
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


class UserCreateView(CreateView): 
 form_class = UserForm
 success_url = '/users_create/'
 template_name = 'users_create_form.html'

class UserLogin(LoginView):
   template_name = "registration/login.html"