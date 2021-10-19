from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.number


class Car(models.Model):
    plate = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.plate


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.owner} | {self.car}"
