from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()


class DriversLicense(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()


class Car(models.Model):
    members = models.ManyToManyField(CarOwner, through='Ownership')
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Ownership(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_b = models.DateField()
    data_c = models.DateField()
