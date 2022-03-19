from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Candies)
admin.site.register(Client)
admin.site.register(Staff)
admin.site.register(Request)