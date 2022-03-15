from django.db import models
from users.models import User
from django.core.validators import MinValueValidator


class Race(models.Model):
    name = models.CharField(max_length=50)
    racers = models.ManyToManyField(User, related_name='races', blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name


class Result(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='results')
    racer = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.racer}, {self.position} место'
