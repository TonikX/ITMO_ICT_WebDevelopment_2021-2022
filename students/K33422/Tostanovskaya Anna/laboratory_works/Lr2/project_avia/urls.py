from django.contrib import admin
from django.urls import path
from . import views
from .views import all_flights
from .views import flight_info
from .views import register
from .views import LoginFormView
from .views import LogoutView


urlpatterns = [
    path('all_flights/', views.all_flights, name='all_flights'),
    path('flight_info/<int:fly_id>/', views.flight_info, name='flight_info'),
    path('register/', views.register, name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]