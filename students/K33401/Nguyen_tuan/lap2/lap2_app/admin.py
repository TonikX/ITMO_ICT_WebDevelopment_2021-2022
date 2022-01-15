from django.contrib import admin
from lap2_app.models import Client, Comment, Bill, Room, Hotel
# Register your models here.
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Bill)
admin.site.register(Room)
admin.site.register(Hotel)
