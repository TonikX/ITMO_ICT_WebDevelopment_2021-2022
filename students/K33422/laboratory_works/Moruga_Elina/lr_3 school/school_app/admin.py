from django.contrib import admin
from django.conf import settings
from .models import *

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentsGroup)
admin.site.register(Teaching)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Timetable)
admin.site.register(Grades)
admin.site.register(Groups)

