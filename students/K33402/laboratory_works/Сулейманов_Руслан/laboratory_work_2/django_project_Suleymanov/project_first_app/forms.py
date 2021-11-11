from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birthday",
        ]