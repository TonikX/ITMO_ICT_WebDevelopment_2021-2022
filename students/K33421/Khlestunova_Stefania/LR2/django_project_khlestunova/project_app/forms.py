from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            "username", "password", "first_name","last_name",
            "doc_data"
        ]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text", "rating",
            "user", "reservation"
        ]