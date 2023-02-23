from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, City, Favourite

admin.site.register(User)
admin.site.unregister(Group)

admin.site.register(City)
admin.site.register(Favourite)
