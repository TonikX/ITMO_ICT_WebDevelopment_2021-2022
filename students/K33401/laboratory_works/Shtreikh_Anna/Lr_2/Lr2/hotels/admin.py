from django.contrib import admin
from hotels.models import Hotel
from hotels.models import Room
from hotels.models import Reservation

admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Room)