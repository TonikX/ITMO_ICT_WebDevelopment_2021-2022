from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    passport = models.CharField(max_length=20, blank=True, null=True)
    home_address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)

user = get_user_model()

class Owner(models.Model):
    owner = models.ForeignKey(user, on_delete=CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateTimeField()

class Driver_Licence(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    receiving_date = models.DateTimeField()

class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)

class Ownership(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=CASCADE)
    car_id = models.ForeignKey(Car, on_delete=CASCADE)
    beginning_date = models.DateTimeField()
    ending_date = models.DateTimeField()

