from django.contrib import admin
from .models import Client, Comment, Bill, Room, Hotel


admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Bill)
admin.site.register(Room)
admin.site.register(Hotel)
