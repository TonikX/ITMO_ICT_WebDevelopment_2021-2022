from datetime import timedelta
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rooms.models import Room


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start = models.DateField()
    end = models.DateField()
    price = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    @property
    def duration(self):
        return (self.end - self.start).days

    def clean(self):
        # Check that start < end
        if self.start >= self.end:
            raise ValidationError("End date must be greater than start date")
        # Check that this booking does not intersect any other bookings for same room
        day = timedelta(days=1)
        intersecting_bookings = self.room.bookings.filter(
            Q(start__range=(self.start, self.end - day)) | Q(end__range=(self.start + day, self.end)))
        if intersecting_bookings.exists() and (
                intersecting_bookings.count() > 1 or intersecting_bookings.first() != self):
            raise ValidationError("Booking dates intersect")

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        self.price = self.room.price * self.duration
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.pk} in hotel {self.room.hotel.name} from {self.start} to {self.end}"
