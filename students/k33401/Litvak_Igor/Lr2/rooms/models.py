from django.db import models
from django.contrib.auth.models import User
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

