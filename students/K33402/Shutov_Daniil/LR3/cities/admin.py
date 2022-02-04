from django.contrib import admin
from cities.models import City, CityPreference

# Register your models here.
admin.site.register(City)
admin.site.register(CityPreference)
