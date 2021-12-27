from django.contrib import admin

from .models import Owner, DriverLicense, Car, Property

admin.site.register(Owner)
admin.site.register(DriverLicense)
admin.site.register(Car)
admin.site.register(Property)
