from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Team, RacerProfile, Race, RacerRegistration, Commentator, Comment


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_type"
    )
    fieldsets = (
        ('Account', {'fields': ('email', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name')}),
        ('Person type', {'fields': ('type',)}),
    )
    add_fieldsets = (
        ('Account', {'fields': ('email', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name')}),
        ('Person type', {'fields': ('type',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(RacerProfile)
admin.site.register(Race)
admin.site.register(RacerRegistration)
admin.site.register(Commentator)
admin.site.register(Comment)
