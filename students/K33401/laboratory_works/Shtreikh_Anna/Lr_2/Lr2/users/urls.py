from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log),
    path('registration/', views.registration),
    path('profile/', views.profile),
    path('logout/', views.log_out),
]
