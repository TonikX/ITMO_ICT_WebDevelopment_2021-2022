from django import forms
from .models import Owner
  
  
class ExampleForm(forms.ModelForm):

      class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "date_of_birth"
        ]