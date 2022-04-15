from django import forms
from .models import Comment, User, Bill
  
  
class UserForm(forms.ModelForm):
      class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "sex",
            "passport",
            "address",
            "natinality"
        ]


class  BookForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            "time",
            "date_start",
            "check_in",
            "check_out",
            "id_room",
            "id_user"
        ]


class CommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
            "time",
            "rate",
            "id_user"
        ]