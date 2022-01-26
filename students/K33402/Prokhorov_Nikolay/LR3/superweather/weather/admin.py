from django.contrib import admin
from .models import *


@admin.register(City)
class CityModel(admin.ModelAdmin):
    pass


@admin.register(WeatherCurrent)
class WeatherCurrentModel(admin.ModelAdmin):
    pass


@admin.register(WeatherDaily)
class WeatherDailyModel(admin.ModelAdmin):
    pass


@admin.register(WeatherForecast)
class WeatherForecastModel(admin.ModelAdmin):
    pass


@admin.register(FavoriteCity)
class FavoriteCityModel(admin.ModelAdmin):
    list_display = ('user', 'city')
