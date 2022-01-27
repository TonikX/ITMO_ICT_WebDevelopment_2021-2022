from django import forms
from .models import Owner


# creating a form
class OwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Owner

        fields = [
            "first_name",
            "last_name",
            "birthday",
        ]
