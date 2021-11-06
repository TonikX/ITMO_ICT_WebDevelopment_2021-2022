from django import forms
from .models import User


# form - create owner
class OwnerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "date_of_birth",
            "passport",
            "home_address",
            "nationality",
        ]
