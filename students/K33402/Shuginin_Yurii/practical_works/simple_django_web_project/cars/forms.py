from django import forms
from cars.models import Car_owner


class CarOwnerCreateForm(forms.ModelForm):

    class Meta:
        model = Car_owner
        fields = ["surname", "name", "birthday"]
