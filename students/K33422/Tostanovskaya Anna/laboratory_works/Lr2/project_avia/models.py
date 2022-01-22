from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    contacts = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Flight(models.Model):
    number = models.CharField(max_length=10)
    flight_company = models.ForeignKey(Company,on_delete=models.CASCADE)
    departure = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival = models.DateTimeField(auto_now=False, auto_now_add=False)
    type_ex = (
        ('up', 'отправление'),
        ('down', 'прибытие'),
    )
    type = models.CharField(max_length=15, choices=type_ex)
    gate_num = models.CharField(max_length=5)

    def __str__(self):
        return self.number


class Comment(models.Model):
    kind_x = (
        ('gate', 'Изменение gate №'),
        ('depart', 'Проблемы с прилетом'),
        ('arrive', 'Проблемы с отправлением'),
        ('lost', 'Потерявшийся пассажир'),
    )
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=False)
    kind = models.CharField(max_length=25, choices=kind_x)
    flight_num = models.ForeignKey(Flight, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)