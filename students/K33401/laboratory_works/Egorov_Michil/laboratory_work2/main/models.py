from django.contrib.auth.models import User
from django.db import models


class Pupil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    father_name = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    grade = models.CharField(max_length=128)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def from_post(post):
        username = post['username']
        password = post['password']
        first_name = post['first_name']
        last_name = post['last_name']

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name)
        user.save()

        father_name = post['father_name']
        grade = post['grade']
        school = post['school']

        pupil = Pupil.objects.create(
            user=user,
            father_name=father_name,
            grade=grade,
            school=school
        )

        return pupil

    def __str__(self):
        return self.full_name
