from django.contrib import admin
from django.contrib.admin import TabularInline

from receipts.models import Receipt, ReceiptItem, ReceiptItemPart


class ReceiptItemInline(TabularInline):
    model = ReceiptItem
    extra = 0
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    inlines = [ReceiptItemInline]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ReceiptItem)
class ReceiptItemAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ReceiptItemPart)
class ReceiptItemPartAdmin(admin.ModelAdmin):
    pass
