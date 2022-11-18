from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
from city_app.models import CityList

class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    birthday = models.DateField(null=True)
    cities = models.ManyToManyField(CityList, through='Membership')

    def __str__(self):
        return f'{self.username}'

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(CityList, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.date_joined}'