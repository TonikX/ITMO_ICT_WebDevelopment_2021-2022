from django.db import models

# Create your models here.

class Car_owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField(blank=True)


class Driver_license(models.Model):
    license_owner = models.ForeignKey(Car_owner,on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30, blank=True)
    owner = models.ManyToManyField(Car_owner, through='Ownership')


class Ownership(models.Model):
    owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True)

