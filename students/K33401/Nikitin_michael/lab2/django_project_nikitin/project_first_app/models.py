from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)

    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)


class DriverLicense(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    license_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()


class Car(models.Model):
    plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    owner = models.ManyToManyField(Driver, through='Ownership', through_fields=('car', 'owner'))

    def __str__(self):
        return f'{self.brand}, {self.model}, {self.color}, {self.plate}'


class Ownership(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    expiration_date = models.DateField(null=True)