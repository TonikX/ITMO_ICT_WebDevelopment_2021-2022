from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView


urlpatterns = [
    path("signin/", LoginView.as_view(next_page="/", template_name="users/sign_in.html")),
    path("signup/", RegistrationView.as_view()),
    path("logout/", LogoutView.as_view(next_page="/"))
]
