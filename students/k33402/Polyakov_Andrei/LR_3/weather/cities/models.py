from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    id = models.IntegerField("Unique id of city", primary_key=True)
    name = models.CharField("City name", max_length=100)

    def __str__(self):
        return str(self.name)


class CityPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="preferences")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="preferences")

    def __str__(self):
        return f"{self.user.username} - {self.city.name}"