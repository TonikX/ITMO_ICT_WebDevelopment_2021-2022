from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone

class User(AbstractUser):
    tel = models.CharField("telephone", max_length=20, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']
    def __str__(self):
        return self.username
class Floor(models.Model):
    number = models.SmallIntegerField(default='0')

class Status(models.Model):
    name = models.CharField(max_length=20, default='')

class Type(models.Model):
    name = models.CharField(max_length=20, default='')
    price = models.IntegerField(default='0')

class Room(models.Model):
    name = models.IntegerField(default='0')
    phone = models.CharField(max_length=20, default='')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)

class Guest(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(default=django.utils.timezone.now)
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    passport = models.CharField(max_length=50, default='')

class Staff(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    date_of_birth = models.DateField(default=django.utils.timezone.now)
    phone = models.CharField(max_length=20, default='')
    adress = models.CharField(max_length=20, default='')

class Bill(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    check_in = models.DateField(default=django.utils.timezone.now)
    check_out = models.DateField(default=django.utils.timezone.now)
    adults = models.SmallIntegerField(default='0')
    children = models.SmallIntegerField(default='0')
    amount = models.IntegerField(default='0')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)

class Schedule(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)
