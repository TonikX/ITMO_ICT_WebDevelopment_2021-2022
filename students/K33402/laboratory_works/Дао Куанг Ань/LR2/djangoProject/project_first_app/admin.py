from django.contrib import admin
from hotel.models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Feedback)
admin.site.register(Bill)
admin.site.register(Room)
admin.site.register(Hotel)