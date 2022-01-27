from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()


class Airport(models.Model):
    name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)


class Flight(models.Model):
    company = models.ForeignKey(
        'tickets.Company',
        on_delete=models.CASCADE,
        related_name='flights'
    )
    departure_airport = models.ForeignKey(
        'tickets.Airport',
        on_delete=models.CASCADE,
        related_name='flights_departure'
    )
    arrival_airport = models.ForeignKey(
        'tickets.Airport',
        on_delete=models.CASCADE,
        related_name='flights_arrival'
    )
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    price = models.FloatField()

    def flight_length(self):
        return self.arrival_datetime - self.departure_datetime


class FlightBookings(models.Model):
    flight = models.ForeignKey(
        'tickets.Flight',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
