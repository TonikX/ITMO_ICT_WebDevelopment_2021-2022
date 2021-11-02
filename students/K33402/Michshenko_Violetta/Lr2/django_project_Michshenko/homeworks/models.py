from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User

class Homework(models.Model):
    lesson = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    due_to = models.DateTimeField()
    text = models.TextField()
    info = models.IntegerField()

    def __str__(self):
        return self.lesson

class Done(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.IntegerField(default = 0)

    def __str__(self):
        return f'ДЗ по {self.homework.lesson} от {self.student.username}'



# Create your models here.
