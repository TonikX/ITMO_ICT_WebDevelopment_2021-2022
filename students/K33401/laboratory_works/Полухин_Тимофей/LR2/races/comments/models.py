from django.db import models
from users.models import User
from races.models import Race
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Comment(models.Model):
    class Type(models.TextChoices):
        COOPERATION = 'COOP', _('Cooperation issue')
        RACES = 'RACE', _('Racing question')
        OTHER = 'OTHER', _('Other')

    type = models.CharField(max_length=15, choices=Type.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField()
    mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.race}, {self.user}, {self.type}, {self.text}'
