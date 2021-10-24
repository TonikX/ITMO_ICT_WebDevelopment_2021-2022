from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from board.models import Assignment, Task


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(required='required', maxlength='30')
        self.fields['last_name'].widget.attrs.update(required='required', maxlength='30')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class AssignmentStudentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["solution"]
        widgets = {
            'solution': forms.Textarea(attrs={'maxlength': 500, 'cols': 38, 'required': 'true'}),
        }


class AssignmentGradeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].widget.attrs.update(required='required')

    class Meta:
        model = Assignment
        fields = ["grade"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["discipline", "title", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'maxlength': 500, 'cols': 38, 'required': 'true'}),
        }