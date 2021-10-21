from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(required='required')
        self.fields['last_name'].widget.attrs.update(required='required')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
