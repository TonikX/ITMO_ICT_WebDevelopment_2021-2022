from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    img = models.CharField(max_length=300, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return "Title: {},address: {}, rate: {}, price: {}".format(self.title, self.address, self.rate, self.price)


class Reserve(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_count = models.IntegerField()

    def __str__(self):
        return "hotel: {}, guest: {}".format(self.hotel.title, self.guest)


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.author.username
