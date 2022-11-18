from django.contrib import admin
from city_app.models import CityList


@admin.register(CityList)
class CityListAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
