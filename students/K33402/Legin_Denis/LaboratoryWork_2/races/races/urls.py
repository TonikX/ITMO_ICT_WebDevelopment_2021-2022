from django.urls import path
from . import views

app_name = 'races'

urlpatterns = [
    path('races/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('races/register', views.register, name='register'),
    path('races/unregister', views.unregister, name='unregister'),
    path('races/', views.RacesView.as_view(), name='races'),
]
