from django.contrib import admin
from .models import Users, Tours, Bookings, Reviews

admin.site.register(Users)
admin.site.register(Tours)
admin.site.register(Bookings)
admin.site.register(Reviews)