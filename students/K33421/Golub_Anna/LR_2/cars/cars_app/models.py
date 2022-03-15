from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.CharField(max_length=300, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        if self.is_superuser:
            return 'superuser'
        return self.last_name + ' ' + self.first_name


class Car(models.Model):
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    RED = 'RED'
    BLUE = 'BLUE'
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    YEAR_IN_SCHOOL_CHOICES = [
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color = models.CharField(
        max_length=30,
        choices=YEAR_IN_SCHOOL_CHOICES
    )

    def __str__(self):
        return self.model


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()
