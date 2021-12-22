from django import forms
from .models import Car, CarOwner

  
  
# creating a form
class ExampleForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner
  
        # specify fields to be used
        fields = [
            "last_name",
            "name",
            "date_b",
        ]
