from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Введите логин", error_messages={'required': 'Обязательное поле'})
    first_name = forms.CharField(max_length=30, required=True, label="Введите Ваше имя", error_messages={'required': 'Обязательное поле'})
    last_name = forms.CharField(max_length=30, required=True, label="Введите Вашу фамилию", error_messages={'required': 'Обязательное поле'})
    password1 = forms.CharField(max_length=30, required=True, label="Введите пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})
    password2 = forms.CharField(max_length=30, required=True, label="Повторите выбранный пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','password1', 'password2', )


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=3000,required=False, widget=forms.Textarea, label="Введите Ваш комментарий")
    TYPES = (
        ('gate', 'Изменение gate №'),
        ('arrival', 'Проблемы с прилетом'),
        ('depart', 'Проблемы с отправлением'),
        ('lost', 'Потерявшийся пассажир'),
    )
    comment_type = forms.CharField(max_length=7, widget=forms.Select(choices=TYPES), label="Отметьте тип вопроса", error_messages={'required': 'Обязательное поле'})

    class Meta:
        model = Comment
        fields = ('comment', 'comment_type', )