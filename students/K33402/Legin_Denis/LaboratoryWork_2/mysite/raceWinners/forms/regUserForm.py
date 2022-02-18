from django import forms
from raceWinners.models import Users


# creating a form
class RegUserForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Users

        # specify fields to be used
        fields = [
            "username",
            "password",
        ]