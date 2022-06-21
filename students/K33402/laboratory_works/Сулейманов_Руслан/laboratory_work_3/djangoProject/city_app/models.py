from django.db import models


class CityList(models.Model):
    city_cod = models.IntegerField('код города')
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    coord_lon = models.FloatField()
    coord_lat = models.FloatField()

    def __str__(self):
        return self.name
