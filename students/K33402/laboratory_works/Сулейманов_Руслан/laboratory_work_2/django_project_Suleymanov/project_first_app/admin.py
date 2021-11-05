from django.contrib import admin
from .models import Owner, Ownership, Car, License
# Register your models here.

admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(License)