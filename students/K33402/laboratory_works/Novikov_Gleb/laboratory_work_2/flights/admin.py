from django.contrib import admin
from .models import Company, Flight, Booking


admin.site.register(Company)
admin.site.register(Flight)
admin.site.register(Booking)
