from datetime import datetime

from django.db import models
from users.models import User
# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Room(models.Model):
    ROOM_TYPE = (
        ('1R','One room'),
        ('2R', 'Two rooms'),
        ('3R', 'Three rooms'),
        ('LUX', 'Lux')
    )
    number = models.IntegerField()
    type = models.CharField(max_length=50, choices=ROOM_TYPE)
    cost = models.FloatField()
    bulk = models.FloatField()
    comfort = models.CharField(max_length=50, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()