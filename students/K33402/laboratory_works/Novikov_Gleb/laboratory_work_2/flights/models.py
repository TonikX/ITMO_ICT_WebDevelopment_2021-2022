from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Company model
class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField("Name", max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


# Flight model
class Flight(models.Model):
    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"

    class TypeChoices(models.IntegerChoices):
        DEPARTING = 0, "Start"
        ARRIVING = 1, "End"

    number = models.CharField("№", max_length=255, unique=True)
    from_city = models.CharField("From city", max_length=255)
    to_city = models.CharField("To city", max_length=255)
    departure_time = models.DateTimeField("Start time")
    arrival_time = models.DateTimeField("End time")
    type = models.IntegerField("Start/end", choices=TypeChoices.choices)
    gate = models.CharField("Gate", max_length=255)
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE,
                                related_name="flights")

    def __str__(self):
        return str(self.number)


# Booking model
class Booking(models.Model):
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    flight = models.ForeignKey(Flight, verbose_name="Flight", on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, related_name="bookings")
    seats = models.IntegerField("Count", validators=[MinValueValidator(1)])
    review_text = models.TextField("Review", default="")
    review_number = models.IntegerField("Score", null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return str(self.id)
