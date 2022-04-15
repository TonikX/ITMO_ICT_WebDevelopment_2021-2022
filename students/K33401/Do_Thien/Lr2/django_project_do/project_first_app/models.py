from django.db import models
#from django.db.models.enums import Choices

class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.date_of_birth)

class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    member = models.ManyToManyField(Owner, through='Possession')
    def __str__(self):
        return "{} {} {} {}".format(self.license_plate, self.brand, self.model, self.color)

class Possession(models.Model):
    owner_possession = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_possession = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Driver_license(models.Model):
    TYPE_LICENSE = (
        ('1', 'STANDARD'),
        ('2', 'FEDERAL'),
        ('3', 'MINISTRY OF INTERNAL AFFAIRS'),
        ('4', 'DIPLOMATIC'),
        ('5', 'ARMED'),
        ('6', 'ROUTE VEHICLE'),
        ('7', 'EXPORTED'),
        )
    owner_license = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    kind = models.CharField(max_length=10, choices=TYPE_LICENSE)
    date_of_issue = models.DateField()
