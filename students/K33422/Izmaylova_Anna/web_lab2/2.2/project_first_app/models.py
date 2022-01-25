from django.db import models

class CarOwner (models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_b = models.DateField()

class License (models.Model): 
    car_owner_id = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

class Car (models.Model):
    gov_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)
    owners = models.ManyToManyField(CarOwner, through='OwnerShip')

class OwnerShip (models.Model):
    car_owner_id = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
