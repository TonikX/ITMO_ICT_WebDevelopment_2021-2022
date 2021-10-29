from django.db import models


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_data = models.DateField()


class DriversLicense(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()


class Car(models.Model):
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Ownership(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_b = models.DateField()
    data_c = models.DateField()
