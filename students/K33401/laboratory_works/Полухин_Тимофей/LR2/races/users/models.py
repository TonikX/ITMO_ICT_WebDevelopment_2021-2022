from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    team = models.CharField(max_length=50, null=True)
    car_description = models.CharField(max_length=100)
    experience = models.CharField(max_length=1000, null=True)
    driver_class = models.CharField(max_length=50)
