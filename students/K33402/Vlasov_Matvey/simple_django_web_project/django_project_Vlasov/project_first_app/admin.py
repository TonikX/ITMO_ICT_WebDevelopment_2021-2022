from django.contrib import admin
from .models import OwnerUser, License, Car, Ownership

admin.site.register(OwnerUser)
admin.site.register(License)
admin.site.register(Car)
admin.site.register(Ownership)
