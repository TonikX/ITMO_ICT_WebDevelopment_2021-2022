from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ["booking", "text", "rating", "made_on"]
    readonly_fields = ["made_on"]
