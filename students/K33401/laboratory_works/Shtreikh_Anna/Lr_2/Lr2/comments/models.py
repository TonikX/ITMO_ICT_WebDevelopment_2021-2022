from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
from hotels.models import Room

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    arrival = models.DateField(blank=True, null=True)
    departure = models.DateField(blank=True, null=True)
    text = models.CharField(max_length=500)
    rate = models.IntegerField(default=1, null=True,
                               validators=[
                                   MaxValueValidator(10),
                                   MinValueValidator(1)
                               ])

