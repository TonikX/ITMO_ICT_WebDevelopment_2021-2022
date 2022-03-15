"""django_project_dao URL Configuration

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
from project_first_app import views

urlpatterns = [
    path('admin/', admin.site.urls)
    , path('owner/', views.detail1)
    , path('owner/<id>', views.detail2)
    , path('time/', views.time_view)
    , path('car/', views.CarView.as_view())
    , path('car/<int:pk>/', views.CarDetailView.as_view())
    , path('car/list/', views.CarListView.as_view())
    , path('owner_post', views.owner_post)
    , path('car/<int:pk>/update/', views.CarUpdateView.as_view())
    , path('car/<int:pk>/delete/', views.CarDeleteView.as_view())
    , path('car/create', views.CarCreateView.as_view(success_url="/car/list/"))
]
