from django.db import models
import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class Client(AbstractUser):
    Birthday = models.DateField(default=django.utils.timezone.now)
    Sex = models.CharField(max_length=10 ,default='')
    Phone = models.IntegerField(default='0')
    Nationality =models.CharField(max_length=20, default='')
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
class Comment(models.Model):
    Client = get_user_model()
    Name_hotel= models.CharField(max_length=500, default='')
    Content = models.CharField(max_length=500, default='')
    Check_in = models.DateField(default=django.utils.timezone.now)
    Check_out = models.DateField(default=django.utils.timezone.now)
    Rate = models.IntegerField(default='0')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
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
class Bill(models.Model):
    Client = get_user_model()
    Date = models.DateField(default=django.utils.timezone.now)
    Check_in = models.DateField(default=django.utils.timezone.now)
    Check_out = models.DateField(default=django.utils.timezone.now)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)


