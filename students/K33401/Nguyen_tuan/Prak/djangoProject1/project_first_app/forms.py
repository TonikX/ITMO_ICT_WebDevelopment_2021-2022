from django import forms
from .models import Car_Owner


# creating a form
class ExampleForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car_Owner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "Date_of_Birth",
        ]