from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Reserve)
admin.site.register(Review)
