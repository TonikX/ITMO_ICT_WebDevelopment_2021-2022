from django.contrib import admin
from .models import Auto, Owner, Ownership, DrivingLicense

admin.site.register(Auto)
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(DrivingLicense)