from django.contrib.auth.forms import UserCreationForm
from .models import CarOwner
  
  
# creating a form
class OwnerForm(UserCreationForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner
  
        # specify fields to be used
        fields = UserCreationForm.Meta.fields+(
            "last_name",
            "first_name",
            "birth_date",
            "passport",
            "address",
            "nationality",
        )