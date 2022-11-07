from django.forms import ModelForm
from .models import Done

class DoneForm(ModelForm):
    class Meta:
        model = Done
        fields = ['text', 'homework']