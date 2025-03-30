from django import forms
from .models import CarOwner
# creating a form
class CarOwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner

        # specify fields to be used
        fields = [
            "surname",
            "name",
            "birthdate",
            "passport",
            "address",
            "nationality"
        ]
