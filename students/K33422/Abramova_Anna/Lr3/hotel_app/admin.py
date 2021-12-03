from django.contrib import admin
from django.contrib.admin import ModelAdmin

from hotel_app.models import Admin, Room, Client, Inhabitation, Cleaner, Cleaning


@admin.register(Admin)
class AdminAdmin(ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    pass


@admin.register(Inhabitation)
class InhabitationAdmin(ModelAdmin):
    pass


@admin.register(Cleaner)
class CleanerAdmin(ModelAdmin):
    pass


@admin.register(Cleaning)
class CleaningAdmin(ModelAdmin):
    pass

