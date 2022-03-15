from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):
    discipline = models.CharField(max_length=30)
    prof = models.TextField(max_length=30)
    post_date = models.DateField()
    due_date = models.DateField()
    assignment = models.TextField(max_length=500)
    penalty = models.TextField(max_length=50)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.discipline, self.post_date)


class User(AbstractUser):
    tasks = models.ManyToManyField('Task', through='Entry')


class Entry(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    submission = models.TextField(max_length=500)
    grade = models.CharField(max_length=1)

