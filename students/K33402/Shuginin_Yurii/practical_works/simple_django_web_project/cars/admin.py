from django.contrib import admin

# Register your models here.

from .models import Car_owner, Driver_license, Car, Ownership

admin.site.register(Car_owner)
admin.site.register(Driver_license)
admin.site.register(Car)
admin.site.register(Ownership)
