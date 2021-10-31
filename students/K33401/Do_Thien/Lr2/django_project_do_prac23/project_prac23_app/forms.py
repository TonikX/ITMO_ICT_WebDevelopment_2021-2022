from django import forms
from .models import OwnerUser
  
  
class ExampleForm(forms.ModelForm):

      class Meta:
        model = OwnerUser
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "passport",
            "address",
            "country"
        ]