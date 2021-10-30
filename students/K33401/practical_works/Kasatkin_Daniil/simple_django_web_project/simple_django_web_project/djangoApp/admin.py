from django.contrib import admin

from .models import CarOwner, Car, DriversLicense, Ownership, user

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriversLicense)
admin.site.register(user)