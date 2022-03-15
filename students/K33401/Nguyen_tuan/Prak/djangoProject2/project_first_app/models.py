from django.db import models
import django.utils.timezone
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class OwerUser(AbstractUser):
    date_of_birthday = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, default='-')
    nationality = models.CharField(max_length=50, default='-')
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
class Driver_license(models.Model):
    OwerUser=get_user_model()
    id_owner = models.ForeignKey(OwerUser,on_delete=models.CASCADE)
    id_number = models.IntegerField(max_length=10, default='-')
    type_of = models.CharField(max_length=10, default='-')
    data_of_issue = models.DateField(default=django.utils.timezone.now)
class Car(models.Model):
    OwerUser = get_user_model()
    state_number = models.CharField(max_length=15, default='-')
    brand = models.CharField(max_length=20, default='-')
    model = models.CharField(max_length=20, default='-')
    color = models.CharField(max_length=30, default='-')
    member = models.ManyToManyField(OwerUser, through='Ownership')
class Ownership(models.Model):
    OwerUser = get_user_model()
    id_owner = models.ForeignKey(OwerUser,on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateField(default=django.utils.timezone.now)
    end_date = models.DateField(default=django.utils.timezone.now)