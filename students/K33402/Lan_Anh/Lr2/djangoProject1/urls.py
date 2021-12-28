"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from my_app import views
from my_app.views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('Room/<id>', views.detail),
    path('Room/', views.detail1),
    path('createbill/', views.create_bill),
    path('createcomment/', views.create_comment),
    path('createclient/', views.create_client),
    path('Client/<id>', views.detail2),
    path('Client/', views.detail3),
    path('Bill/', views.detail4),
    path('bill/<int:pk>/update/',BillUpdateView.as_view()),
    path('bill/<int:pk>/delete/',BillDeleteView.as_view()),
    path('bill/find/',detail5),
]
