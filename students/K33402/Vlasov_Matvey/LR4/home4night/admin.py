from django.contrib import admin
from .models import *

admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Review)
