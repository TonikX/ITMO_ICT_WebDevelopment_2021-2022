from django.contrib import admin
from .models import Owner, Car, auto_Owner, ID_owner

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(auto_Owner)
admin.site.register(ID_owner)