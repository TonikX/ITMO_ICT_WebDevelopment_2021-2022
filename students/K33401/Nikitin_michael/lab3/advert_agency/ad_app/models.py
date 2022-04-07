from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Worker(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    clients = models.ManyToManyField(Client, through='Application', blank=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Service(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Application(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.service} для {self.client}'


class Assignment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.application}'
