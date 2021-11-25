from datetime import timedelta
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.CharField(max_length=255)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='owned_hotels')

    def __str__(self):
        return f"{self.stars}-star hotel {self.name}"


class Room(models.Model):
    number = models.CharField(max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    beds = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    smoking_allowed = models.BooleanField(default=False)
    price = models.PositiveIntegerField()

    class Meta:
        # One hotel can't have two rooms with the same number
        unique_together = ['number', 'hotel']

    def __str__(self):
        return f"Room {self.number} of hotel {self.hotel.name}"


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
        if intersecting_bookings.count() > 1 or intersecting_bookings.first() != self:
            raise ValidationError("Booking dates intersect")

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        nights = (self.end - self.start).days
        self.price = self.room.price * nights
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.pk} in hotel {self.room.hotel.name} from {self.start} to {self.end}"
