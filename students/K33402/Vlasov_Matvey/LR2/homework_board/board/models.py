from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    class Meta:
        verbose_name_plural = "classes"

    name = models.CharField(max_length=5)
    disciplines = models.ManyToManyField(Discipline, related_name='classes')

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class_school = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Assignment(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.discipline}: {self.title}"


class Submission(models.Model):
    class Grade(models.IntegerChoices):
        EXCELLENT = 5, '5'
        GOOD = 4, '4'
        FAIR = 3, '3'
        POOR = 2, '2'

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500, blank=True)
    grade = models.IntegerField(choices=Grade.choices, null=True, blank=True)

    def __str__(self):
        return f"""{self.assignment.discipline}: {self.assignment.title} |
         {self.student.user.first_name} {self.student.user.last_name} |
         Grade: {self.grade}"""
