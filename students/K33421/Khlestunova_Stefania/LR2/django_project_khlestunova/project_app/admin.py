from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from project_app.forms import UserForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Airline)
admin.site.register(Plane)
admin.site.register(Users)
admin.site.register(Places)
admin.site.register(Reservation)
admin.site.register(Comment)

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    model = Users
    list_display = ['email', 'username',]