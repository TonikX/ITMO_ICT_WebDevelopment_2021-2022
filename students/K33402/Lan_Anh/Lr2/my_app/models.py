from django.db import models
import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Client(AbstractUser):
    Birthday = models.DateField(default=django.utils.timezone.now)
    Sex = models.CharField(max_length=10 ,default='')
    Phone = models.IntegerField(default='0')
    Nationality =models.CharField(max_length=20, default='')
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Hotel(models.Model):
    Name_hotel = models.CharField(max_length=500, default='')
    Owner = models.CharField(max_length=500, default='')
    Address = models.CharField(max_length=500, default='')
    Describe = models.CharField(max_length=500, default='')

class Room(models.Model):
    Client = get_user_model()
    Number = models.IntegerField(default='0')
    Type = models.CharField(max_length=500, default='')
    Price = models.IntegerField(default='0')
    State = models.CharField(max_length=500, default='')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Member = models.ManyToManyField(Client, through='Bill')

class ClientBookingDetails(models.Model):
    Client = get_user_model()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Check_in = models.DateField(default=django.utils.timezone.now)
    Check_out = models.DateField(default=django.utils.timezone.now)
    class Meta:
        abstract = True

class Comment(ClientBookingDetails):
    Name_hotel= models.CharField(max_length=500, default='')
    Content = models.CharField(max_length=500, default='')
    Rate = models.IntegerField(default='0')

class Bill(ClientBookingDetails):
    Date = models.DateField(default=django.utils.timezone.now)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)