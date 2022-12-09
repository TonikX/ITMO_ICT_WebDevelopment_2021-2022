from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

# Таблица с турами
class Tours(models.Model):
    name = models.CharField(max_length=30)
    firm = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    date_start = models.DateField()
    date_end = models.DateField()
    payment = models.CharField(max_length=30)
    country = models.CharField(max_length=20)

# Таблица с пользователями, которые могу регистрироваться (поэтому в скобках AbstractUser)
# у пользователя есть имя, логин, пароль, они встроены в AbstractUser
class Users(AbstractUser):
    birth_date = models.DateField(null=True)
    bookings_id = models.ManyToManyField(Tours, through='Bookings')

# Таблица с бронированием
class Bookings(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    # администратор сможет подтверждать бронь на туры
    status = models.CharField(max_length=30, choices=(('confirmed','confirmed'), ('not confirmed','not confirmed')), default='not confirmed yet')

# Отзывы
class Reviews(models.Model):
    content = models.CharField(max_length=300)
    SCORE_CHOICES = zip(range(1,10), range(1,10))
    rate = models.IntegerField(choices=SCORE_CHOICES, blank=True)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    id_tour = models.ForeignKey(Tours, on_delete=models.CASCADE) 