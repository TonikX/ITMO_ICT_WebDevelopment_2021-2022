from django.contrib import admin

# Register your models here.

from .models import CarOwnerUser, Driver_license, Car, Ownership

admin.site.register(CarOwnerUser)
admin.site.register(Driver_license)
admin.site.register(Car)
admin.site.register(Ownership)
