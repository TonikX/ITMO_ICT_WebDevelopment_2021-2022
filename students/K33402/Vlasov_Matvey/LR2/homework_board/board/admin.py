from django.contrib import admin

from board.models import Teacher, Discipline, DisciplineAdmin, Class, ClassAdmin, Student, Assignment, Submission

admin.site.register(Teacher)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Submission)