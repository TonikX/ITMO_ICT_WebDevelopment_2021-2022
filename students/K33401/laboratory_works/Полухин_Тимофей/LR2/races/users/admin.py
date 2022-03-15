from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
