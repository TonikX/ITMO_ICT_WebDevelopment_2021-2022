from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, FloatField, ManyToManyField

from weather.fields import IntegerRangeField


class Town(models.Model):
    name = CharField(max_length=200)
    lon = FloatField()
    lat = FloatField()

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    towns = ManyToManyField(Town, blank=True)
    days_count = IntegerRangeField(default=3, min_value=1, max_value=10)
