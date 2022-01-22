from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class City(models.Model):
    """City"""

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    name = models.CharField("City name", max_length=50)
    lat = models.FloatField("Latitude", validators=[MinValueValidator(-180), MaxValueValidator(180)])
    lon = models.FloatField("Longtitude", validators=[MinValueValidator(-180), MaxValueValidator(180)])

    def __str__(self):
        return str(self.name)


class FavouriteCity(models.Model):
    """Favourite city of user"""

    class Meta:
        verbose_name = "Favourite city"
        verbose_name_plural = "Favourite cities"

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="favourites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")

    def __str__(self):
        return f"{self.city.name} ({self.user.username})"
