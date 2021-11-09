from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    passport_id = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class DriversLicense(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()


class Car(models.Model):
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_s = models.DateField()
    data_e = models.DateField()
