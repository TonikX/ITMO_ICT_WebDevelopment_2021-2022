from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.signin, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
