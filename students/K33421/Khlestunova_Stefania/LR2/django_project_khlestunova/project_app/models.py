from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model

# Create your models here.
class Airline(models.Model):
    airline_name = models.CharField(max_length=50)

    def __str__(self):
        return self.airline_name

class Plane(models.Model):
    flight_number = models.CharField(max_length=5, null=False)
    dep_time = models.DateTimeField(verbose_name='departure time')
    ar_time = models.DateTimeField(verbose_name='arrival time')
    f_type = models.CharField(max_length=1, choices=[('1', 'departure'), ('0', 'arrival')])
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.flight_number} | {self.airline}"

class Users(AbstractUser):
    Username = None
    doc_data = models.CharField(max_length=11)
    f_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.f_name + " " + self.last_name

class Places(models.Model):
    User = get_user_model()
    p_number = models.CharField(max_length=3)
    price = models.IntegerField(null=True)
    plane_number = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_number + " | " + self.plane_number.flight_number 

class Reservation(models.Model):
    User = get_user_model()
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.p_number + " | " + self.user.username

class Comment(models.Model):
    rating_List = [
        ('0', 'Awful'),
        ('1', 'Very bad'),
        ('2', 'Very bad'),
        ('3', 'Bad'),
        ('4', 'Bad'),
        ('5', 'Okay'),
        ('6', 'Okay'),
        ('7', 'Good'),
        ('8', 'Good'),
        ('9', 'Excellent'),
        ('10', 'Excellent')
    ]
    User = get_user_model()
    text = models.CharField(max_length=3000)
    rating = models.CharField(max_length=2, choices=rating_List)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.reservation.place.p_number + " | " + self.rating