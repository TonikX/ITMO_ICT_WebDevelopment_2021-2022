from django.contrib import admin
from project_first_app.models import Owner, Car_Owner, Driver_license, Car
# Register your models here.
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Car_Owner)
admin.site.register(Driver_license)
