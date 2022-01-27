from django.contrib import admin
from .models import CarOwner, License, Car, Ownership
from django.contrib.auth.admin import UserAdmin

admin.site.register(CarOwner)
admin.site.register(License)
admin.site.register(Car)
admin.site.register(Ownership)

