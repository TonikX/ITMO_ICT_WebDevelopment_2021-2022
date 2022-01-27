from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    max_occupancy = models.IntegerField()
    is_reserved = models.FloatField(default=False)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserve_time = models.DateTimeField(default=datetime.now, blank=True)
    arrival_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    departure_date = models.DateTimeField(default=datetime.now, blank=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now, blank=True)
    text = models.CharField(max_length=100000, blank=True)
    rate = models.IntegerField(default=1,
                               validators=[
                                   MaxValueValidator(10),
                                   MinValueValidator(1)
                               ])
