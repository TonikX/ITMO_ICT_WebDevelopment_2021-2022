from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    pass


@admin.register(WeatherModel)
class WeatherModelAdmin(admin.ModelAdmin):
    pass


@admin.register(MyCitiesModel)
class MyCitiesModelAdmin(admin.ModelAdmin):
    pass
