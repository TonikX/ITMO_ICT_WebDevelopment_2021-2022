from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass


@admin.register(Cleaning)
class CleaningAdmin(admin.ModelAdmin):
    pass
