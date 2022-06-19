from django.db import models
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
    government_number = models.CharField(max_length=15)
    automark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.automark + " " + self.model


class CarOwner(AbstractUser):
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    connect = models.ManyToManyField(Car, through='Owning', blank=True)
    pasport_number = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.CharField(max_length = 100, blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)


class Owning(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete = models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete = models.CASCADE, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)


class DriversLicense(models.Model):
    car_owner_id = models.ForeignKey(CarOwner, on_delete = models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()


