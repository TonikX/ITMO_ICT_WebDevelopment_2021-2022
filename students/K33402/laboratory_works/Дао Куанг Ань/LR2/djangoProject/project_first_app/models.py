from django.db import models
import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.


class Client(AbstractUser):
    SEX = [("M", "Male"), ("F", "Female"), ("Other", "Other")]
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    birthdate = models.DateField(default=django.utils.timezone.now)
    sex = models.CharField(max_length=10, default='M', choices=SEX)
    tel = models.CharField(max_length=12, default='')
    passport = models.CharField(max_length=10, default="")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Hotel(models.Model):
    name = models.CharField(max_length=50, default='')
    owner = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return "{}".format(self.name)


class Feedback(models.Model):
    Client = get_user_model()
    rating = models.IntegerField(default='5')
    comment = models.CharField(max_length=500, default='')

    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id_client.last_name)


class Room(models.Model):
    TYPE = [("1", "Single"), ("2", "Double"), ("3", "Triple")]
    client = get_user_model()
    number = models.IntegerField(default='0')
    type = models.CharField(max_length=6, default='1', choices=TYPE)
    price = models.IntegerField(default=1000)
    state = models.BooleanField(default=True)

    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_client = models.ManyToManyField(Client, through='Bill')

    def __str__(self):
        return "{} {}".format(self.number, self.id_hotel.name)


class Bill(models.Model):
    Client = get_user_model()
    date_register = models.DateField(default=django.utils.timezone.now)
    date_checkin = models.DateField(default=django.utils.timezone.now)
    date_checkout = models.DateField(default=django.utils.timezone.now)
    time_checkin = models.TimeField(default=django.utils.timezone.now)
    time_checkout = models.TimeField(default=django.utils.timezone.now)

    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.date_checkin, self.date_checkout)
