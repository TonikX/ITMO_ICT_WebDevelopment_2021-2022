from django.contrib import admin
from weather.models import Town, User, Country

admin.site.register(User)
admin.site.register(Town)
admin.site.register(Country)
