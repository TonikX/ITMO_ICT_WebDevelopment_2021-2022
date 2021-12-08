from django.contrib import admin

from .models import Owner, Driver_Licence, Car, Ownership, User

class Owner_Admin(admin.ModelAdmin):
    pass

class Driver_Licence_Admin(admin.ModelAdmin):
    pass

class Car_Admin(admin.ModelAdmin):
    pass

class Ownership_Admin(admin.ModelAdmin):
    pass

class User_Admin(admin.ModelAdmin):
    pass

admin.site.register(Owner, Owner_Admin)
admin.site.register(Driver_Licence, Driver_Licence_Admin)
admin.site.register(Car, Car_Admin)
admin.site.register(Ownership, Ownership_Admin)
admin.site.register(User, User_Admin)