from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Worker(AbstractUser):
    # работник авиакомпании
    id = models.AutoField(unique=True, primary_key=True)
    fio = models.CharField(max_length=100, null=False, verbose_name='ФИО')
    age = models.IntegerField(validators=[MinValueValidator(18)], verbose_name='Возраст', default=18)

    education_types = (
        ('VSH', "Высшее"),
        ('VSN', "Высшее неоконченное"),
        ('SRD', "Среднее"),
        ('SRS', "Среднее специальное"),
    )
    education = models.CharField(choices=education_types, max_length=3, verbose_name='уровень образования')
    stajh_raboty = models.IntegerField(verbose_name='Стаж работы')
    passport = models.CharField(max_length=10, verbose_name='Паспортные данные')
    work = models.ManyToManyField('Ekipazh', through='Aviacompany')

    REQUIRED_FIELDS = ['email', 'stajh_raboty', 'fio']

    def __str__(self):
        return "{}".format(self.fio)


class Ekipazh(models.Model):
    # Экипаж
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Название экипажа")

    def __str__(self):
        return "{}".format(self.name)


class Aviacompany(models.Model):
    # Штаб авиакомпании
    id_ekipazha = models.ForeignKey('Ekipazh', verbose_name="ID экипажа", on_delete=models.CASCADE)
    id_workera = models.ForeignKey('Worker', verbose_name="ФИО работника", on_delete=models.CASCADE)
    work = models.CharField(max_length=30, verbose_name="Занимаемая должность")


class Plane(models.Model):
    # Самолёт
    id = models.AutoField(unique=True, primary_key=True)
    type = models.CharField(max_length=15, verbose_name="Тип")
    number = models.CharField(max_length=8, verbose_name="Номер модели")
    mesta = models.IntegerField(verbose_name="Количество мест")
    speed = models.IntegerField(verbose_name="Скорость полёта (км/ч)")
    avia = models.CharField(max_length=20, verbose_name="Авиакомпания")

    def __str__(self):
        return "{}-{}-{}".format(self.type, self.number, self.avia)


class Razrechenie(models.Model):
    # Разрешение на полёт на данном самолёте
    id_plane = models.ForeignKey('Plane', verbose_name="ID самолёта", on_delete=models.CASCADE)
    id_ekipazha = models.ForeignKey('Ekipazh', verbose_name="Экипаж", on_delete=models.CASCADE)
    razrechenie = models.BooleanField(default=True)


class Remont(models.Model):
    # Самолёты в ремонте
    id = models.AutoField(unique=True, primary_key=True)
    id_plane = models.ForeignKey('Plane', verbose_name="Самолёт", on_delete=models.CASCADE)
    polomka = models.CharField(max_length=100, verbose_name="Поломка")


class Tranzit(models.Model):
    # Пересадки
    id = models.AutoField(unique=True, primary_key=True)
    punkt_peresadki = models.CharField(max_length=20, verbose_name="Пункт пересадки")

    def __str__(self):
        return "{}".format(self.punkt_peresadki)


class Reys(models.Model):
    # Рейс
    number = models.IntegerField(unique=True, primary_key=True)
    distance = models.IntegerField(verbose_name="Расстояние до пункта назначения")
    punkt_start = models.CharField(max_length=20, verbose_name="Пункт вылета")
    punkt_end = models.CharField(max_length=20, verbose_name="Пункт прилёта")
    id_tranzita = models.ForeignKey('Tranzit', verbose_name="Транзит", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}-{}".format(self.number, self.punkt_start, self.punkt_end)


class Dopusk(models.Model):
    # Допуск на рейс
    number_reysa = models.ForeignKey('Reys', verbose_name="Номер рейса", on_delete=models.CASCADE)
    id_ekipazha = models.ForeignKey('Ekipazh', verbose_name="Экипаж", on_delete=models.CASCADE)
    nalichie_dopuska = models.BooleanField(default=True)


class Polet(models.Model):
    # Полёт на самолёте по рейсу
    id_poleta = models.AutoField(unique=True, primary_key=True)
    number_reysa = models.ForeignKey('Reys', verbose_name="Номер-Рейс", on_delete=models.CASCADE)
    id_plane = models.ForeignKey('Plane', verbose_name="Самолёт", on_delete=models.CASCADE)
    date_start = models.DateField(verbose_name="Дата вылета")
    time_start = models.TimeField(verbose_name="Время вылета")
    date_end = models.DateField(verbose_name="Дата прилёта")
    time_end = models.TimeField(verbose_name="Время прилёта")
    sell_tickets = models.IntegerField(verbose_name="Количество проданных билетов")
    made_reys = models.IntegerField(verbose_name="Количество совершённых рейсов")
    date_start_tranzit = models.DateField(verbose_name="Дата транзитной посадки", blank=True, null=True)
    time_start_tranzit = models.TimeField(verbose_name="Время транзитной посадки", blank=True, null=True)
    date_end_tranzit = models.DateField(verbose_name="Дата вылета из транзита", blank=True, null=True)
    time_end_tranzit = models.TimeField(verbose_name="Время вылета из транзита", blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.number_reysa, self.id_plane)