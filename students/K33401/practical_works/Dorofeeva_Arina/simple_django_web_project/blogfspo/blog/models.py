from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DriverLicense(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

    def __str__(self):
        return self.license_number


class Car(models.Model):
    owner = models.ManyToManyField(Owner, through='Property')
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    plate = models.CharField(max_length=15)

    def __str__(self):
        return self.plate


class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    date_of_expiring = models.DateField(null=True)

    def __str__(self):
        return f"{self.owner}: {self.car}"
