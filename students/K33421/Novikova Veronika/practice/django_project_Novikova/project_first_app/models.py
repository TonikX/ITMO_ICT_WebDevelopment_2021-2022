from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):

    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_birth = models.DateTimeField(null=True, blank=True)
    passport = models.CharField(max_length=30, null=True, blank=True)
    adress = models.CharField(max_length=30, null=True, blank=True)
    nationality = models.CharField(max_length=15, null=True, blank=True)


class License(models.Model):

    owner_license = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()


class Car(models.Model):

    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Owning')
    number_car = models.CharField(max_length=15)
    brand_car = models.CharField(max_length=20)
    model_car = models.CharField(max_length=20)
    color_car = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.number_car


class Owning(models.Model):

    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_beginning = models.DateTimeField()
    date_ending = models.DateTimeField(null=True, blank=True)
