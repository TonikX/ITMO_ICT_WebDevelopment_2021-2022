from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tel = models.CharField("Phone number", max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username
    

class Floor(models.Model):
    number = models.SmallIntegerField()

    def __str__(self):
        return "Type: {}".format(self.number)


class Status(models.Model):
    types = (
        ('e', 'empty'),
        ('f', 'full')
    )
    name = models.CharField(max_length=1, choices=types, verbose_name='Status')

    def __str__(self):
        return "Type: {}, Name: {}".format(self.types, self.name)
    

class Type(models.Model):
    types = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    name = models.CharField(max_length=1, choices=types, verbose_name='Type')
    price = models.IntegerField(verbose_name='Price')

    def __str__(self):
        return "Type: {}, Name: {}, Price: {}".format(self.types, self.name, self.price)


class Room(models.Model):
    number = models.CharField(max_length=10, verbose_name='Room number', default='100')
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=CASCADE)
    floor_id = models.ForeignKey(Floor, on_delete=CASCADE)

    def __str__(self):
        return "Number: {}, Status: {}".format(self.number, self.status_id)
    

class Guest(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    middle_name = models.CharField(max_length=30, verbose_name='Middle name', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Birthday')
    address = models.CharField(max_length=50, verbose_name='Address', default='VP 5/7')
    city = models.CharField(max_length=30, verbose_name='City')
    email = models.CharField(max_length=50, verbose_name='Email',blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Phone number', default='897777777')
    passport = models.CharField(max_length=15, default='C5555555')

    def __str__(self):
        return "First name: {}, Last name: {}".format(self.first_name, self.last_name)    


class Staff(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    middle_name = models.CharField(max_length=30, verbose_name='Middle name',blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Birthday', null=True)
    phone = models.CharField(max_length=20, verbose_name='Phone number', null=True)
    address = models.CharField(max_length=50, verbose_name='Address', null=True)

    def __str__(self):
        return "First name: {}, Last name: {}".format(self.first_name, self.last_name)


class Reservation(models.Model):
    date = models.DateField(verbose_name='Date')
    check_in = models.DateField(verbose_name='Check in')
    check_out = models.DateField(verbose_name='Check out')
    adults = models.SmallIntegerField()
    children = models.SmallIntegerField(blank=True, null=True)
    amount = models.IntegerField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return "Date: {}, Check in: {}, Check out: {}".format(self.date, self.check_in, self.check_out)

class Schedule(models.Model):
    date = models.DateField(verbose_name='Date')
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return "Date: {}, Staff: {}, Floor: {}".format(self.date, self.staff_id, self.floor_id)