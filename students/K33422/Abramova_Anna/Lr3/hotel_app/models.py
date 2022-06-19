from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    phone = models.CharField(max_length=14)
    full_name = models.CharField(max_length=255)


class Room(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    cost_of_living = models.IntegerField()
    ROOM_TYPES = [(1, "Одноместный"), (2, "Двуместный"), (3, "Трёхместный")]
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    pasport = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    rooms = models.ManyToManyField(Room, through='Inhabitation')


class Inhabitation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    in_date = models.DateField()
    out_date = models.DateField()


class Cleaner(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    contract_number = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Cleaning(models.Model):
    cleaner = models.ForeignKey(Cleaner, on_delete=models.SET_NULL, null=True)
    cleaning_floor = models.IntegerField()
    cleaning_day = models.DateField()
