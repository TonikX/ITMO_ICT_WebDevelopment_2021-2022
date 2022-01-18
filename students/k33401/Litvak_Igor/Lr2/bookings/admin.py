from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ['room', 'by', 'start', 'end', 'price']
    readonly_fields = ['price']
