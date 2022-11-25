from django.contrib import admin
from .models import CarOwner
from .models import Car
from .models import Owning 
from .models import DriversLicense 

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(Owning)
admin.site.register(DriversLicense)

# Register your models here.
