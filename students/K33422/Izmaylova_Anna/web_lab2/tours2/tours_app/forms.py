from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users, Reviews
  
# форма для регистрации пользователя
class UserForm(UserCreationForm):
   class Meta:
       model = Users
       fields = ['username', 'first_name', 'last_name', 'birth_date', 'email']

# форма для добавления отзыва
class ReviewForm(forms.Form):
    model = Reviews
    fields = ['content', 'rate', 'start_date', 'end_date', 'id_user']
  