from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import LoginView, RegisterView, confirm

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/<str:code>/', confirm, name='confirm')
]
