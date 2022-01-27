from django.contrib import admin
from .models import City, FavouriteCity


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(FavouriteCity)
class FavouriteCity(admin.ModelAdmin):
    pass
