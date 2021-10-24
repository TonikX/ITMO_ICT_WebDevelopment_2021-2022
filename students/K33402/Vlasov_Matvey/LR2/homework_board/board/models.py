from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Class(models.Model):
    class Meta:
        verbose_name_plural = "classes"

    name = models.CharField(max_length=5)
    disciplines = models.ManyToManyField(Discipline, through='ClassDiscipline')

    def __str__(self):
        return self.name


class ClassDiscipline(models.Model):
    class_school = models.ForeignKey(Class, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.class_school.name} {self.discipline.name}'


class ClassDisciplineInline(admin.TabularInline):
    model = ClassDiscipline
    extra = 1


class ClassAdmin(admin.ModelAdmin):
    inlines = (ClassDisciplineInline, )


class DisciplineAdmin(admin.ModelAdmin):
    inlines = (ClassDisciplineInline, )


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class_school = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.discipline}: {self.title}"


class Assignment(models.Model):
    class Grade(models.IntegerChoices):
        EXCELLENT = 5, '5'
        GOOD = 4, '4'
        FAIR = 3, '3'
        POOR = 2, '2'

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500, blank=True)
    last_submission = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(choices=Grade.choices, null=True, blank=True)

    def __str__(self):
        return f"""{self.task.discipline}: {self.task.title} |
         {self.student.user.first_name} {self.student.user.last_name} |
         Grade: {self.grade}"""

    def get_teacher(self):
        teacher = ClassDiscipline.objects.get(class_school=self.student.class_school,
                                              discipline=self.task.discipline).teacher
        return teacher
