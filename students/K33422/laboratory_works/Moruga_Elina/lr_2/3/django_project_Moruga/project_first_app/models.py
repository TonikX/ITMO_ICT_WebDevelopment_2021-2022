from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class CarOwner(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=30, null=True)
    # password = models.CharField(max_length=15, default='')
    # last_login = models.CharField(max_length=15)
    # is_superuser = models.BooleanField()
    # username = models.CharField(max_length=15, unique=True)
    # email = models.CharField(max_length=25)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # date_joined =  models.DateField(null=True)

class License(models.Model):
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_license = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateField()

class Car(models.Model):
    gov_no = models.CharField(max_length=15) 
    brand =  models.CharField(max_length=20)
    model =  models.CharField(max_length=20)
    color =  models.CharField(max_length=30, null=True)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

class Ownership(models.Model):
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id_car = models.ForeignKey(Car,on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)