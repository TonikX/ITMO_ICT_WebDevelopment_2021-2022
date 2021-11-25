from django.contrib import admin
from bookings.models import Hotel, Room, Booking


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'stars', 'owner']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = ['number', 'hotel', 'beds', 'smoking_allowed', 'price']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ['room', 'by', 'start', 'end', 'price']
    readonly_fields = ['price']
