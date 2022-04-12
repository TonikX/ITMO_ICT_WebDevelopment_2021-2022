from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Driver)
admin.site.register(Ownership)

