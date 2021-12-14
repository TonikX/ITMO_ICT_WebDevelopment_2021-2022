from django.contrib import admin
from rooms.models import Hotel, Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'stars', 'owner']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = ['number', 'hotel', 'beds', 'smoking_allowed', 'price']
