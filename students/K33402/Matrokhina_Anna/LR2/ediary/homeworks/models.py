from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Homeworks(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()

    text = models.TextField()
    penalty = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.discipline} {self.teacher.first_name} {self.teacher.last_name} {self.name}'


class HomeworkWork(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homeworks, on_delete=models.CASCADE)

    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    mark = models.IntegerField(blank=True, null=True)
