from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Pair)
admin.site.register(SubjectToTeacher)
admin.site.register(User)