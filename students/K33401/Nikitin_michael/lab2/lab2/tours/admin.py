from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Tour)
admin.site.register(UsersComments)
admin.site.register(Booked)