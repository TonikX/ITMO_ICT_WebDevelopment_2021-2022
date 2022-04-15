from django.contrib import admin

from .models import *


admin.site.register(OwnerUser)
admin.site.register(Car)
admin.site.register(Possession)
admin.site.register(Driver_license)