from django.contrib import admin
from .models import *

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Bill)
admin.site.register(Staff)
admin.site.register(Floor)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Schedule)