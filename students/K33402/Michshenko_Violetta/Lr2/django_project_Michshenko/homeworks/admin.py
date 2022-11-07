from django.contrib import admin
from .models import Homework, Done

@admin.register(Homework)
class Homeworkadmin(admin.ModelAdmin):
    pass

@admin.register(Done)
class Doneadmin(admin.ModelAdmin):
    pass


# Register your models here.
