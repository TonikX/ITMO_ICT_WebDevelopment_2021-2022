from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "username", "password", "first_name","last_name",
            "doc_data"
        ]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "place", "user"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text", "rating",
            "user", "reservation"
        ]