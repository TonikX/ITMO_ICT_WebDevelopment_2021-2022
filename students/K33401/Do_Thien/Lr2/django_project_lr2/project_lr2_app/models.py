from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import django.utils.timezone


class User(AbstractUser):
    date_of_birth = models.DateField(default=django.utils.timezone.now)
    sex = models.CharField(max_length=10)
    passport = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    natinality = models.CharField(max_length=30)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    desrible = models.CharField(max_length=60)
    def __str__(self):
        return "{} {} {} {}".format(self.name, self.owner, self.address, self.desrible)


class Room(models.Model):
    User = get_user_model()
    number = models.SmallIntegerField(null=False)
    type = models.CharField(max_length=15)
    price = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    member = models.ManyToManyField(User, through='Bill')
    def __str__(self):
        return "{} {} {} {}".format(self.number, self.type, self.price, self.status)


class Bill(models.Model):
    User = get_user_model()
    time = models.DateTimeField(default=django.utils.timezone.now)
    date_start = models.DateField(default=django.utils.timezone.now)
    check_in = models.DateField(default=django.utils.timezone.now)
    check_out = models.DateField(default=django.utils.timezone.now)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {} {}".format(self.time, self.date_start, self.check_in, self.check_out)


class Comment(models.Model):
    User = get_user_model()
    content = models.CharField(max_length=100)
    time = models.DateTimeField(default=django.utils.timezone.now)
    rate = models.SmallIntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {}".format(self.content, self.time, self.rate)