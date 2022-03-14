from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, FloatField, ForeignKey, ManyToManyField, IntegerField

from weather.fields import IntegerRangeField

CONTINENTS = (
    ('AS', 'Asia'),
    ('EU', 'Europe'),
    ('NA', 'North America'),
    ('SA', 'South America'),
    ('OC', 'Oceania'),
    ('AF', 'Africa')
)


class Country(models.Model):
    name = CharField(max_length=200)
    continent = CharField(max_length=10, choices=CONTINENTS)

    def __str__(self):
        return f'{self.name} in {self.continent}'


class Town(models.Model):
    name = CharField(max_length=200)
    country = ForeignKey(Country, on_delete=models.CASCADE)
    lon = FloatField()
    lat = FloatField()

    def __str__(self):
        return f'{self.name} in {self.country}'


class User(AbstractUser):
    towns = ManyToManyField(Town, blank=True)
    days_count = IntegerRangeField(default=3, min_value=1, max_value=10)

    # REQUIRED_FIELDS = ['email', 'towns']
