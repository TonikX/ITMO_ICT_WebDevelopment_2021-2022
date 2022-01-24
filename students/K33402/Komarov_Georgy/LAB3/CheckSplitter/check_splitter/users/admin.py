from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User
from utils.admin import ExtendedAdmin


@admin.register(User)
class UserAdmin(ExtendedAdmin, DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'avatar', 'check_scan_token')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
