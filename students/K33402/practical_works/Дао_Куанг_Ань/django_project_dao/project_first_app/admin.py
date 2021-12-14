from django.contrib import admin
from project_first_app.models import Owner, Ownership, Car, License

# Register your models here.
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(License)