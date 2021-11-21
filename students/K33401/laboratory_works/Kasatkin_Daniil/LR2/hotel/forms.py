from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['arrival_date', 'departure_date']
        exclude = ['user', 'room', 'reserve_time', 'comment']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
            'text': forms.Textarea(attrs={'rows': 30, 'cols': 100, 'placeholder': 'Type your comment...'}),
        }
        fields = ['text', 'rate']
        exclude = ['user', 'create_time']
