from django.db import models
from django.contrib.auth.models import User


# Для выбранного пользователем города храним только его ID, потому что остальная информация есть на фронте
class ChosenCity(models.Model):
    class Meta:
        unique_together = ['city_id', 'user']

    city_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cities")
