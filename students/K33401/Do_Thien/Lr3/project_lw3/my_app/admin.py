from django.contrib import admin
from .models import *


admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Staff)
admin.site.register(Schedule)