from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type_choices = [
        ('admin', 'администратор'),
        ('deputy', 'замдекана'),
        ('manager', 'диспетчер'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, verbose_name='Тип')

    REQUIRED_FIELDS = ('type', 'first_name', 'last_name')

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subjects = models.ManyToManyField('Subject', through='SubjectToTeacher')
    room = models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class SubjectToTeacher(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.teacher, self.subject)


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.CharField(max_length=40)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Mark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.student.last_name, self.subject)


class Pair(models.Model):
    day_choices = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]
    group = models.CharField(max_length=40)
    pair_number = models.IntegerField()
    name_day = models.CharField(max_length=30, choices=day_choices)
    room = models.IntegerField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} пара №'.format(self.name_day, self.group, self.pair_number)
