from django import forms
from .models import User


# creating a form
class CarOwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = ['first_name', 'last_name', 'birth_date', 'nation', 'passport_id', 'address']
