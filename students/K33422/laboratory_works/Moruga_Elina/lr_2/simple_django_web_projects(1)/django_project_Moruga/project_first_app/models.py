from django.db import models

class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)

class License(models.Model):
    id_owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    id_license = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateField()

class Car(models.Model):
    gov_no = models.CharField(max_length=15) 
    brand =  models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    color =  models.CharField(max_length=30, null=True)

class Ownership(models.Model):
    id_owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car,on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    expiration_date = models.DateField(null=True)