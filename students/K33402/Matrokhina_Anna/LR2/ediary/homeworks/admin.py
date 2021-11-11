from django.contrib import admin

from .models import Discipline, Homeworks, HomeworkWork


# Register your models here.
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(Homeworks)
class HomeworksAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'teacher', 'name', 'date')


@admin.register(HomeworkWork)
class HomeworkWorkAdmin(admin.ModelAdmin):
    pass
