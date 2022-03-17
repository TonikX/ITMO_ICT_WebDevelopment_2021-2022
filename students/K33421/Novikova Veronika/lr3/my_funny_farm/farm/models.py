from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    cage = models.ManyToManyField('Cage', through="Working")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Chicken(models.Model):
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    egg_amount = models.IntegerField(default=0)
    cage = models.ForeignKey('Cage', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.breed} {self.cage}'


class Breed(models.Model):
    breed = models.CharField(max_length=50)
    avg_eggs = models.IntegerField(default=0)
    avg_weight = models.IntegerField(default=0)
    diet = models.TextField()

    def __str__(self):
        return self.breed


class Cage(models.Model):
    shed = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    cage = models.IntegerField(default=0)
    square = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.shed} {self.row} {self.cage}'


class Working(models.Model):
    types = (
        ("clean", "clean"),
        ("feed", "feed"),
        ("med", "give medicine")
    )
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    cage = models.ForeignKey('Cage', on_delete=models.CASCADE)
    work = models.CharField(max_length=20, choices=types)

