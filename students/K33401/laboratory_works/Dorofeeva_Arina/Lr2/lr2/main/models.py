from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Conference(models.Model):
    name = models.CharField("conference", max_length=50)
    topic = models.CharField("topic", blank=True, choices=[
        ("IT", "IT"),
        ("business", "business"),
        ("economics", "economics"),
    ], max_length=10)
    location = models.CharField("location", max_length=100)
    start_date = models.DateField("start date")
    end_date = models.DateField("end date")
    description = models.CharField("conference description", max_length=200)
    location_description = models.CharField("location description", max_length=200)
    terms = models.CharField("participation terms", max_length=1000)
    speaker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="speaker", null=True)

    class Meta:
        verbose_name = "conference"
        verbose_name_plural = "conferences"

    def __str__(self):
        return f"{self.topic}: {self.name}"


class Comment(models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, verbose_name="conference"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="comment author"
    )
    text = models.CharField("comment", max_length=100)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.author}: {self.text}"
