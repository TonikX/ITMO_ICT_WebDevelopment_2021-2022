from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    favourite_cities = models.ManyToManyField('City', verbose_name='Favourites', through='Favourite', related_name='UserFavourites')


class City(models.Model):
    """City"""

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    name = models.CharField("City name", max_length=50)

    def __str__(self):
        return str(self.name)


class Favourite(models.Model):
    """User's favourite city"""

    class Meta:
        verbose_name = "Favourite"
        verbose_name_plural = "Favourites"
        unique_together = ["city", "user"]

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="favourites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")

    def __str__(self):
        return f"{self.user.username} - {self.city.name}"
