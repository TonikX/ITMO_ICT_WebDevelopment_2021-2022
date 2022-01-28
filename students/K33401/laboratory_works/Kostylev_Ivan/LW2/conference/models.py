from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Conference(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.name}\nAbout {self.topic}\n{self.description}\nWhere: {self.place}\n When:{self.date}\n' \
               f'Conditions: {self.conditions}'


# class Registration(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
#     is_approved = models.BooleanField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f'User: {self.user.username}\nAbout conf: {self.conference.name}\nRating: ' \
               f'{self.rating}\nReview:\n{self.description}'
