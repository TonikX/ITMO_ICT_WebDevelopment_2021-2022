from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    name = models.CharField(max_length=100)


class Conference(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    is_approved = models.BooleanField()
    date = models.DateTimeField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
