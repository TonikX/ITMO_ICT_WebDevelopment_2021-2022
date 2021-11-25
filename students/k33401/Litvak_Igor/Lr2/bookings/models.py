from datetime import timedelta
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Hotel(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='owned_hotels')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    beds = models.PositiveIntegerField()
    smoking_allowed = models.BooleanField(default=False)
    price = models.PositiveIntegerField()


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start = models.DateField()
    end = models.DateField()
    price = models.PositiveIntegerField()

    def clean(self):
        # Check that start < end
        if self.start >= self.end:
            raise ValidationError("End date must be greater than start date")
        # Check that this booking does not intersect any other bookings for same room
        day = timedelta(days=1)
        intersecting_bookings = self.room.bookings.filter(
            Q(start__range=(self.start, self.end - day)) | Q(end__range=(self.start + day, self.end)))
        if intersecting_bookings.exists():
            raise ValidationError("Booking dates intersect")

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        nights = (self.end - self.start).days
        self.price = self.room.price * nights
        super(Booking, self).save(*args, **kwargs)
