from django.contrib import admin

from accounts.models import User, Membership


class MembershipInline(admin.TabularInline):
    model = Membership


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False
