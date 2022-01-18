from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class GroupModel(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, blank=True, null=True)


class TeacherModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SubjectModel(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class HometaskModel(models.Model):
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    published = models.DateTimeField()
    deadline = models.DateTimeField()
    description = models.TextField()
    penalty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}: {}".format(self.subject, self.description)


class SubmissionModel(models.Model):
    hometask = models.ForeignKey(HometaskModel, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    grade = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('hometask', 'user', "grade")
