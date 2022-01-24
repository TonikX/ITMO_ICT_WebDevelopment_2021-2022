from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)

    lat = models.FloatField()
    lon = models.FloatField()

    local_names = models.JSONField()


class WeatherCurrent(models.Model):
    class Meta:
        verbose_name = 'Текущий прогноз'
        verbose_name_plural = 'Текущие прогнозы'

    dt = models.FloatField()
    sunrise = models.FloatField(blank=True, null=True)
    sunset = models.FloatField(blank=True, null=True)
    temp = models.FloatField()
    feels_like = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    dew_point = models.FloatField()
    uvi = models.FloatField()
    clouds = models.FloatField()
    visibility = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    weather = models.JSONField()
    wind_gust = models.FloatField(blank=True, null=True)
    pop = models.FloatField(blank=True, null=True)


class WeatherForecast(models.Model):
    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    current = models.OneToOneField(WeatherCurrent, on_delete=models.CASCADE, related_name='forecast')

    lat = models.FloatField()
    lon = models.FloatField()

    timezone = models.CharField(max_length=128)
    timezone_offset = models.IntegerField()

    minutely = models.JSONField()
    hourly = models.JSONField()
    alerts = models.JSONField()

    date_created = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.current.delete()
        return super().delete(using, keep_parents)


class WeatherDaily(models.Model):
    class Meta:
        verbose_name = 'Прогноз по дням'
        verbose_name_plural = 'Прогнозы по дням'

    forecast = models.ForeignKey(WeatherForecast, related_name='daily', on_delete=models.CASCADE)
    weekday = models.IntegerField()

    dt = models.FloatField()
    sunrise = models.FloatField()
    sunset = models.FloatField()
    moonrise = models.FloatField()
    moonset = models.FloatField()
    moon_phase = models.FloatField()
    temp = models.JSONField()
    feels_like = models.JSONField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    dew_point = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    wind_gust = models.FloatField()
    weather = models.JSONField()
    clouds = models.FloatField()
    pop = models.FloatField()
    snow = models.FloatField(blank=True, null=True)
    uvi = models.FloatField()


class FavoriteCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
