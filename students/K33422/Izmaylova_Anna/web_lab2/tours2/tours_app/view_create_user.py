from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Users
from .forms import UserForm
from django.contrib.auth.views import LoginView

# представление для создания пользователя 
class UserCreateView(CreateView): 
   form_class = UserForm
   success_url = '/users_create/' # куда перейдет сайт, когда мы успешно зарегистируемся
   template_name = 'users_create_form.html'


# представление для входа на сайт
class UserLogin(LoginView):
   template_name = "registration/login.html"