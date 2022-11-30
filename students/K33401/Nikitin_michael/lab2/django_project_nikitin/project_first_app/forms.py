from django import forms
from .models import Driver


# creating a form
class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = [
            'surname',
            'name',
            'date_of_birth',
        ]