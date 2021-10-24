from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from board.models import Submission


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(required='required', maxlength='30')
        self.fields['last_name'].widget.attrs.update(required='required', maxlength='30')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["solution"]
        widgets = {
            'solution': forms.Textarea(attrs={'maxlength': 500, 'cols': 38, 'required': 'true'}),
        }