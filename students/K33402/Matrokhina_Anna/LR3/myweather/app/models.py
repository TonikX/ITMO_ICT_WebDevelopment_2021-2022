from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CityModel(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    local_names = models.JSONField()


class WeatherModel(models.Model):
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name='weather')
    lat = models.FloatField()
    lon = models.FloatField()
    current = models.JSONField()
    daily = models.JSONField()


class MyCitiesModel(models.Model):
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
