"""djangoProject URL Configuration

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
from django.urls import path
from hotel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bill/', bill),
    path('bill/create/', BillCreateView.as_view()),
    path('bill/update/<int:pk>/', BillUpdateView.as_view()),
    path('bill/delete/<int:pk>/', BillDeleteView.as_view()),
    path('client/', client),
    path('client/update/<int:pk>/', ClientUpdateView.as_view()),
    path('client/create/', ClientCreateView.as_view()),
    path('feedback/', fb),
    path('feedback/create/', FeedbackCreateView.as_view()),
    path('room/', room),
    path('client/<id>/', client_id),
    path('clm/', c_last_month),
]
