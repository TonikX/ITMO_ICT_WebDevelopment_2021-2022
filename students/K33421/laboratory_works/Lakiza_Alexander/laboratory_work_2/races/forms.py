from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from .models import Comment, RacerProfile, Team, RacerRegistration

User = get_user_model()


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(label="User type", choices=[(1, "Racer"), (2, "Viewer")])

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def clean_user_type(self):
        a = self.cleaned_data['user_type']
        print("user_type", a)
        return a

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            user_type=self.cleaned_data['user_type']
        )
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
        return user


class CustomRacerCreationForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    description = forms.CharField(label="Description", max_length=120)
    experience = forms.CharField(label="Experience", max_length=120)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CustomRacerCreationForm, self).__init__(*args, **kwargs)

    def clean_team(self):
        team = self.cleaned_data['team']
        return team

    def clean_description(self):
        description = self.cleaned_data['description']
        return description

    def clean_experience(self):
        experience = self.cleaned_data['experience']
        return experience

    def save(self, commit=True):
        racerProfile = RacerProfile.objects.create(
            base_user=self.user,
            team=self.cleaned_data['team'],
            description=self.cleaned_data['description'],
            experience=self.cleaned_data['experience'],
            raiting=1
        )
        return racerProfile


class RaceRegistrationForm(forms.Form):
    car = forms.CharField(label="Car", max_length=90)

    def __init__(self, *args, **kwargs):
        self.racer = kwargs.pop('racer', None)
        self.race = kwargs.pop('race', None)
        super(RaceRegistrationForm, self).__init__(*args, **kwargs)

    def clean_car(self):
        car = self.cleaned_data['car']
        return car

    def save(self, commit=True):
        racerRegistration = RacerRegistration.objects.create(
            racer=self.racer,
            race=self.race,
            car=self.cleaned_data['car']
        )
        return racerRegistration


class RaceEditRegistrationForm(forms.Form):
    car = forms.CharField(label="Car", max_length=90)

    def __init__(self, *args, **kwargs):
        self.raceRegistration = kwargs.pop('race_reg', None)
        super(RaceEditRegistrationForm, self).__init__(*args, **kwargs)

    def clean_car(self):
        car = self.cleaned_data['car']
        return car

    def save(self, commit=True):
        print(self.raceRegistration.car)
        print(self.cleaned_data['car'])
        self.raceRegistration.car = self.cleaned_data['car']
        self.raceRegistration.save()
        return self.raceRegistration


class CommentForm(forms.Form):
    text = forms.CharField(max_length=300, label="Question text")
    comment_type = forms.ChoiceField(choices=(
        (1, "Вопрос о сотрудничестве"),
        (2, "Вопрос о гонках"),
        (3, "Иное")
    ), label="Question type")

    def __init__(self, *args, **kwargs):
        self.commentator = kwargs.pop('commentator', None)
        self.race = kwargs.pop('race', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clear_text(self):
        text = self.cleaned_data['text']
        return text

    def clear_comment_type(self):
        comment_type = self.cleaned_data['comment_type']
        print(comment_type)
        return comment_type

    def save(self, commit=True):
        comment = Comment.objects.create(
            commentator=self.commentator,
            race=self.race,
            text=self.cleaned_data['text'],
            comment_type=self.cleaned_data['comment_type']
        )
        return comment
