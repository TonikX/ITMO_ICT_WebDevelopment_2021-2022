from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.DateTimeField(null=True)

class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateField(null=False)

    def __str__(self):
        return self.number

class Car(models.Model):
    gos_number = models.CharField(max_length=15, null=False)
    mark = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True)
