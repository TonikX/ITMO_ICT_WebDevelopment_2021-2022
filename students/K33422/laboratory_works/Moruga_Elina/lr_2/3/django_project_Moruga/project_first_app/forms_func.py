from django import forms
from .models import CarOwner
  
  
# creating a form
class OwnerForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner
  
        # specify fields to be used
        fields = [
            "Last name",
            "First name",
            "Birth date",
            "Passport",
            "Address",
            "Nationality"
        ]