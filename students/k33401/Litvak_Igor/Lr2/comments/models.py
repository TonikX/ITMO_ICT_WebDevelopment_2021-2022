from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from bookings.models import Booking


class Comment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(blank=True, default="")
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    made_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on room {self.booking.room} or hotel {self.booking.room.hotel}"
