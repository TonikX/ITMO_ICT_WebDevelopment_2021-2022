from django.db import models
import django.utils.timezone
from django.contrib.auth.models import AbstractUser

class HotelUser(AbstractUser):
    SEX_TYPES = (
        ('M', 'male'),
        ('F', 'female'),
        ('N', 'N/A')
    )
    sex = models.CharField(max_length=10 , choices=SEX_TYPES, verbose_name="Sex")
    phone = models.CharField(max_length=20, verbose_name="Phone")

    def __str__(self):
        return "User: {} {}".format(self.first_name, self.last_name)

class Visitor(HotelUser):
    VISITOR_TYPES = (
        ('A', 'adult'),
        ('C', 'children')
    )
    birthday = models.DateField(default=django.utils.timezone.now, verbose_name="Visitor Birthday")
    nationality = models.CharField(max_length=20, default='', verbose_name='Nationality')
    passport_no = models.CharField(max_length=20 , blank=False, verbose_name='Passport number')
    visitor_type = models.CharField(max_length=1, choices=VISITOR_TYPES, verbose_name='Visitor types')

    class Meta:
         verbose_name = "Visitor"

class Host(HotelUser):
    LICENSE_TYPES = (
        ('I', 'Certificate I'),
        ('II', 'Certificate II'),
        ('III', 'Certificate III'),
        ('IV', 'Certificate IV'),
    )
    license = models.CharField(max_length=20, blank=False, choices=LICENSE_TYPES, verbose_name="License")
    workExp = models.IntegerField(default='0', blank=False, verbose_name="Work Experience")

    class Meta:
         verbose_name = "Host"

class Hotel(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name="Name of Hotel")
    address = models.CharField(max_length=100, default='', verbose_name="Address")
    description = models.CharField(max_length=200, default='', verbose_name="Hotel description")

    owner = models.ForeignKey(Host, null=True, verbose_name="Hotel Owner", on_delete=models.SET_NULL)
    
    def __str__(self):
        return "Hotel: {}".format(self.name)

class Room(models.Model):
    STATE_TYPES = (
        ('AV', 'Available'),
        ('NA', 'Not Available'),
        ('MA', 'On maintainence')
    )
    number = models.IntegerField(default='0', verbose_name='Number')
    price = models.IntegerField(default='0', verbose_name='Price')
    state = models.CharField(max_length=500, choices=STATE_TYPES, verbose_name='State')
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE, verbose_name='Hotel Id')

    def __str__(self):
        return "Room: {} of Hotel: {}".format(self.number, self.hotel.name)

class Booking(models.Model):
    booking_code = models.CharField(max_length=10, blank=False, verbose_name='Booking Code')
    date_checkin = models.DateField(default=django.utils.timezone.now, verbose_name='Date Checkin')
    date_checkout = models.DateField(default=django.utils.timezone.now, verbose_name='Date Checkout')
    main_guest = models.ForeignKey(Visitor, related_name='bookings', null=True, verbose_name='Main guest', on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, verbose_name='Room', null=True, on_delete=models.DO_NOTHING)


    def __str__(self):
        return "Booking: {}".format(self.booking_code)

class Bill(models.Model):
    service_name = models.CharField(max_length=100, blank=False, verbose_name='Service Name')
    description = models.CharField(max_length=500, default='', verbose_name='Description')
    total = models.IntegerField(default='0', blank=False, verbose_name="Total Cost of Service")

    booking = models.ForeignKey('Booking', related_name='bills', null=True, verbose_name='Booking Id', on_delete=models.DO_NOTHING);

    def __str__(self):
        return "Bill: {} of Booking {}".format(self.service_name, self.booking)