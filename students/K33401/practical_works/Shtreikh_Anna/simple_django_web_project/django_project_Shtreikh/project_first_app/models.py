from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CarOwner(AbstractUser):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    passport = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)

class Car(models.Model):
    gos_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class Hold(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    begin = models.DateField(null=False)
    end = models.DateField()

class License(models.Model):
    car_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    ex_date = models.DateField(null=False)

