from django.db import models
from django.contrib.auth.models import AbstractUser


class Candies(models.Model):
    id_candy = models.IntegerField(unique=True)
    type = models.CharField(max_length=50, verbose_name='Type')
    description = models.CharField(max_length=11, verbose_name='Description')
    price = models.IntegerField(verbose_name='Price', null=True)

    def __str__(self):
        return f"{self.id_candy}"


class Request(models.Model):
    id_req = models.IntegerField(unique=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    candies = models.ForeignKey('Candies', on_delete=models.CASCADE, verbose_name='Candies')
    req_date = models.DateField(verbose_name='Request date')


class Client(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    passport = models.CharField(max_length=11, verbose_name='Passport')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    number = models.IntegerField(verbose_name='Id number')
    REQUIRED_FIELDS = ['last_name', 'first_name', 'patronymic',
                       'passport', 'number']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Staff(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    duty = models.IntegerField(verbose_name='Duty')
    working_days = models.CharField(max_length=10, verbose_name='Working_days')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"