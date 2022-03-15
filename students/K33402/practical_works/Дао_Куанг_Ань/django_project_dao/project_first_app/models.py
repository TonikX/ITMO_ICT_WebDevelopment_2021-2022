from django.db import models
import django.utils.timezone


# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя", default="-")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия", default="-")
    date_of_birth = models.DateField(verbose_name="Дата рождения", default=django.utils.timezone.now)
    description = models.TextField(default="-")

    def __str__(self):
        return self.first_name, self.last_name


class Car(models.Model):
    state_number = models.CharField(max_length=15, verbose_name="Гос номер", default="-")
    brand = models.CharField(max_length=20, verbose_name="Марка", default="-")
    model = models.CharField(max_length=20, verbose_name="Модель", default="-")
    color = models.CharField(max_length=30, verbose_name="Цвет", default="-")

    members = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return "{} {} {} {}".format(self.state_number
                                    , self.brand
                                    , self.model
                                    , self.color)


class Ownership(models.Model):
    start_date = models.DateField(verbose_name="Дата начала", default=django.utils.timezone.now)
    end_date = models.DateField(verbose_name="Дата окончания", default=django.utils.timezone.now)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class License(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, verbose_name="Номер удостоверения")
    type = models.CharField(max_length=10, verbose_name="Тип", default="-")
    date_of_issue = models.DateField(verbose_name="Дата выдачи", default=django.utils.timezone.now)
