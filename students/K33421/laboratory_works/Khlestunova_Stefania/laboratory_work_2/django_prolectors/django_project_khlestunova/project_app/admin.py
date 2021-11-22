from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Airline)
admin.site.register(Plane)
admin.site.register(Users)
admin.site.register(Places)
admin.site.register(Reservation)
admin.site.register(Comment)