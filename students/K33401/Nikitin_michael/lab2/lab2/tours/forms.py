from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booked, UsersComments


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "passport",
            "is_admin",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = UsersComments
        fields = [
            "rate",
            "text",
        ]