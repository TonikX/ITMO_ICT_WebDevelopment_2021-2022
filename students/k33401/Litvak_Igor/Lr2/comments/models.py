from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from bookings.models import Booking


class Comment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
