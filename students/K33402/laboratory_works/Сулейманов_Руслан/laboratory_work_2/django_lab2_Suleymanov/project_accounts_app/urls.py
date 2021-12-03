from django.urls import path,re_path
from allauth.account.views import SignupView, LoginView, LogoutView, EmailView, EmailVerificationSentView, ConfirmEmailView
from . import views

class MySignupView(SignupView):
    template_name = 'account/signup.html'

class MyLoginView(LoginView):
    template_name = 'account/login.html'

class MyLogoutView(LogoutView):
    template_name = 'account/logout.html'

class MyEmailView(EmailView):
    template_name = 'account/email.html'

class MyEmailVerificationSentView(EmailVerificationSentView):
    template_name = 'account/verification_sent.html'

class MyConfirmEmailView(ConfirmEmailView):
    template_name = 'account/email_confirm.html'

urlpatterns = [
    path("email/", MyEmailView, name="account_email"),
    path(
        "confirm-email/",
        MyEmailVerificationSentView,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        MyConfirmEmailView,
        name="account_confirm_email",
    ),
    path('login/', MyLoginView.as_view(), name='account_login'),
    path('signup/', MySignupView.as_view(), name='account_signup'),
    path('logout/', MyLogoutView.as_view(), name='account_logout'),
    path('', views.account, name='account'),
]