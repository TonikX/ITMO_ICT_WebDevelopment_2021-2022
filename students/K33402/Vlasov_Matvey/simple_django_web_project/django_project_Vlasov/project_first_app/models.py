from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class OwnerUser(AbstractUser):
    birthday = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class License(models.Model):
    OwnerUser = get_user_model()
    owner = models.ForeignKey(OwnerUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.number


class Car(models.Model):
    OwnerUser = get_user_model()
    plate = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(OwnerUser, through='Ownership')

    def __str__(self):
        return self.plate


class Ownership(models.Model):
    OwnerUser = get_user_model()
    owner = models.ForeignKey(OwnerUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.owner} | {self.car}"
