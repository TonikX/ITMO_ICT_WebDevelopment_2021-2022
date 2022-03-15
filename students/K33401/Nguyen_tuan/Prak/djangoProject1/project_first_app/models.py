# Create your models here.
from django.db import models
from django.conf import settings
import django.utils.timezone

class Car_Owner(models.Model):
    first_name = models.CharField(max_length=30, default='-')
    last_name = models.CharField(max_length=30, default='-')
    Date_of_Birth = models.DateField(default=django.utils.timezone.now)
    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.Date_of_Birth)
class Car(models.Model):
    state_number = models.CharField(max_length=15, default='-')
    brand = models.CharField(max_length=20, default='-')
    model = models.CharField(max_length=20, default='-')
    Color = models.CharField(max_length=30, default='-')
    def __str__(self):
        return "{} {} {} {}".format(self.state_number, self.brand, self.model, self.Color)
    member = models.ManyToManyField(Car_Owner, through='Owner')
class Owner(models.Model):
    id_owner = models.ForeignKey(Car_Owner,on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateField(default=django.utils.timezone.now)
    end_date = models.DateField(default=django.utils.timezone.now)
class Driver_license(models.Model):
    id_owner = models.ForeignKey(Car_Owner,on_delete=models.CASCADE)
    id_number = models.IntegerField(max_length=10, default='-')
    type_of = models.CharField(max_length=10, default='-')
    data_of_issue = models.DateField(default=django.utils.timezone.now)

