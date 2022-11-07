"""django_project_Michshenko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homeworks.views import HomeworkListView, DoneCreateView, marks
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeworks/', HomeworkListView.as_view(), name = 'homework'),
    path('register', CreateView.as_view(template_name = 'register.html', form_class = UserCreationForm, success_url='/homeworks')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('homeworks/submit', DoneCreateView.as_view(), name = 'done'),
    path('marks/',marks, name='marks'),
]
