from django.urls import path
from django.contrib.auth.views import LoginView
from auth.views import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
