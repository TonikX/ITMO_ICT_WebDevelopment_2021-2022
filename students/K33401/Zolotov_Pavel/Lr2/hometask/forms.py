from django import forms

from hometask.models import SubmissionModel


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = SubmissionModel
        fields = ['hometask', 'text']
