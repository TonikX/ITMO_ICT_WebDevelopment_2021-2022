from django import forms
from .models import Owner

class Owner_Form(forms.ModelForm):
    class Meta():
        model = Owner
        fields = ["first_name", "last_name", "date_birth", "owner"]