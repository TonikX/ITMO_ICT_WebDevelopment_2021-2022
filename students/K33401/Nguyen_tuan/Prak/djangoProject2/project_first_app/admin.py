from django.contrib import admin
from project_first_app.models import Ownership, OwerUser, Driver_license, Car
# Register your models here.
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(OwerUser)
admin.site.register(Driver_license)