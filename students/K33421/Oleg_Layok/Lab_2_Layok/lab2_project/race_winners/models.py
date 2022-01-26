from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
class User(AbstractUser):
    DEFAULT_PK = 1
    user_type = models.IntegerField(choices=[
        (1, "Racer"),
        (2, "Viewer")
    ], default=1)


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class RacerProfile(models.Model):
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='racer_info', primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    experience = models.CharField(max_length=90)
    raiting = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.base_user.username + ' ' + self.description


class Race(models.Model):
    DEFAULT_PK = 500
    name = models.CharField(max_length=45)
    racer_list = models.ManyToManyField(RacerProfile, through='RacerRegistration')
    date = models.DateField(default=datetime.date.today)
    result = models.CharField(max_length=160, default="Не известен")

    def __str__(self) -> str:
        return self.name + ' ' + str(self.date)


class RacerRegistration(models.Model):
    racer = models.ForeignKey(RacerProfile, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    car = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.racer.base_user.username + ' -> ' + self.race.name


class Commentator(models.Model):
    DEFAULT_PK = 1000
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    raiting = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.user_info.username + "  Рейтинг: " + str(self.raiting)


class Comment(models.Model):
    commentator = models.ForeignKey(Commentator, on_delete=models.CASCADE, default=Commentator.DEFAULT_PK)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, default=Race.DEFAULT_PK)
    text = models.CharField(max_length=210)
    time = models.DateTimeField(default=datetime.datetime.now)
    comment_type = models.IntegerField(choices=[
        (1, "Вопрос о сотрудничестве"),
        (2, "Вопрос о гонках"),
        (3, "Иное")
    ])

    def __str__(self) -> str:
        return self.commentator.user_info.username + ' -> ' + self.text