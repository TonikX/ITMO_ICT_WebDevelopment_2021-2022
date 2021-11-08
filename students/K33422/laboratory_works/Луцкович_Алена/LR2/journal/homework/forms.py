from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Entry


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class AddEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['student', 'task', 'submission']
