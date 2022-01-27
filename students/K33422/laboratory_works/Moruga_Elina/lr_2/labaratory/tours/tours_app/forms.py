from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users, Reviews
  
  
# creating a form
class UserForm(UserCreationForm):
   class Meta:
       model = Users
       fields = ['username', 'first_name', 'last_name', 'birth_date', 'email']

class ReviewForm(forms.Form):

    model = Reviews
    fields = ['content', 'rate', 'start_date', 'end_date', 'id_user']
  