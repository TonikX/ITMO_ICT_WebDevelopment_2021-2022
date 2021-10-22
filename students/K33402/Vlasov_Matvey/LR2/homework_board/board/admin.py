from django.contrib import admin

from board.models import Teacher, Discipline, Class, Student, Assignment, Submission

admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Submission)