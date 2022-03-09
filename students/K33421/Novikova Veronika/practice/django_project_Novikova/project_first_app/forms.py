from django import forms
from .models import Owner, Car


class Create_owner_form(forms.ModelForm):

    class Meta:

        model = Owner

        fields = [
            'last_name',
            'first_name',
            'date_birth',
            'passport',
            'adress',
            'nationality',
        ]
