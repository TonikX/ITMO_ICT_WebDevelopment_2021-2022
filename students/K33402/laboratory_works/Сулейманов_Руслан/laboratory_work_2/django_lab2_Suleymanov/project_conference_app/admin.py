from django.contrib import admin

# Register your models here.
from project_conference_app.models import Topic, Conference, Comments, Performance

admin.site.register(Topic)
admin.site.register(Conference)
admin.site.register(Performance)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'conference', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
