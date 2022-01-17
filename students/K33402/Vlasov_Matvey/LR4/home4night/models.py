from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Property(models.Model):
    owner = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    guest_limit = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    price = models.IntegerField(validators=[MaxValueValidator(100000), MinValueValidator(1)])
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.city} | {self.title}'


class Booking(models.Model):
    STATUS = (
        ('UNPAID', 'UNPAID'),
        ('PAID', 'PAID'),
        ('CANCELLED', 'CANCELLED'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    total_price = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=10, default='Unpaid')

    def __str__(self):
        return f'{self.property.city} | {self.property.title} | {self.checkin} - {self.checkout}'


class Review(models.Model):
    class Grade(models.IntegerChoices):
        EXCELLENT = 5, '5'
        GOOD = 4, '4'
        FAIR = 3, '3'
        POOR = 2, '2'
        BAD = 1, '1'

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True)
    grade = models.IntegerField(choices=Grade.choices)
    comment = models.CharField(max_length=500, blank=True)
    last_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.booking.property.city} | {self.booking.property.title} | Grade: {self.grade}'




