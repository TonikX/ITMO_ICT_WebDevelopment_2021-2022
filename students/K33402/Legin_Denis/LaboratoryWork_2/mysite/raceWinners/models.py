from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)


class Racers(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    car = models.CharField(max_length=50)


class RaceRacers(models.Model):
    racer = models.ForeignKey(Racers, on_delete=models.CASCADE)
    racerRate = models.IntegerField()


class Race(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    dateTime = models.DateTimeField()
    racers = models.ForeignKey(RaceRacers, on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField()
    comment_type = models.CharField(max_length=100)
    comment_text = models.CharField(max_length=500)
    rate = models.IntegerField()
