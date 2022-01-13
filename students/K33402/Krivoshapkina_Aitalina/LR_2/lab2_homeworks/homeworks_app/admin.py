from django.contrib import admin

# Register your models here.

from .models import User, Course, Homework, StudentHomework

# Register your models here.
admin.site.register(User)
admin.site.register(Homework)
admin.site.register(Course)
admin.site.register(StudentHomework)

