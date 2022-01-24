from django import forms
from cars.models import CarOwnerUser


class CarOwnerCreateForm(forms.ModelForm):

    class Meta:
        model = CarOwnerUser
        fields = ["username", "password", "surname", "name", "birthday", "passport", "home_address", "nationality"]
