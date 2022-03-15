from django.db import models
import django.utils.timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    tel = models.CharField(max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class Employee(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    salary = models.IntegerField(default=30000)
    passport = models.CharField(max_length=10, default="")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Client(models.Model):
    SEX = [("M", "Male"), ("F", "Female"), ("Other", "Other")]
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    birthdate = models.DateField(default=django.utils.timezone.now)
    sex = models.CharField(max_length=10, default='M', choices=SEX)
    tel = models.CharField(max_length=12, default='')
    city = models.CharField(max_length=50, default='')
    passport = models.CharField(max_length=10, default="")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Room(models.Model):
    TYPE = [("1", "Single"), ("2", "Double"), ("3", "Triple")]
    STATE = [("+", "Available"), ("-", "Occupied")]
    number = models.IntegerField(default='0')
    type = models.CharField(max_length=6, default='1', choices=TYPE)
    price = models.IntegerField(default=1000)
    floor = models.SmallIntegerField(default='1')
    state = models.CharField(max_length=9, default="+", choices=STATE)

    employee = models.ManyToManyField(Employee, through='Schedule')
    client = models.ManyToManyField(Client, through='Bill')

    def __str__(self):
        return "{}".format(self.number)


class Schedule(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    time = models.TimeField(default=django.utils.timezone.now)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.date, self.time)


class Bill(models.Model):
    date_register = models.DateField(default=django.utils.timezone.now)
    date_checkin = models.DateField(default=django.utils.timezone.now)
    date_checkout = models.DateField(default=django.utils.timezone.now)
    time_checkin = models.TimeField(default=django.utils.timezone.now)
    time_checkout = models.TimeField(default=django.utils.timezone.now)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.date_checkin, self.date_checkout)
