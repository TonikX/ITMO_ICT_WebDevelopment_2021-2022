from django.contrib import admin

from .models import User, Car, DriversLicense, Ownership


admin.site.register(User)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriversLicense)
