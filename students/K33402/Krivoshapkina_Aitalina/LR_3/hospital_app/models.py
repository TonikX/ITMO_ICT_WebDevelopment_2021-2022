from django.db import models
import datetime


weekdays = (
   ('mon', 'monday'),
   ('tue', 'tuesday'),
   ('wed', 'wednesday'),
   ('thu', 'thursday'),
   ('fri', 'friday'),
   ('sat', 'saturday'),
   ('sun', 'sunday'),
)

class Patient(models.Model):
   first_name = models.CharField(max_length=120, verbose_name='Имя пациента')
   last_name = models.CharField(max_length=120, verbose_name='Фамилия пациента')

   def __str__(self):
      return self.first_name + " " + self.last_name


class Specialization(models.Model):
   title = models.CharField(max_length=120, verbose_name='Название специализации')
   description = models.TextField(verbose_name='Описание')

   def __str__(self):
      return self.title


# class Schedule(models.Model):
#    weekday = models.CharField(max_length=120, choices=weekdays, verbose_name='День недели')


class Doctor(models.Model):
   sex_types = (
      ('f', 'female'),
      ('m', 'male')
   )
   education_types = (
      ('bch', 'bachelor'),
      ('phd', 'Ph.D.')
   )
   first_name = models.CharField(max_length=120, verbose_name='Имя доктора')
   last_name = models.CharField(max_length=120, verbose_name='Фамилия доктора')
   specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE, verbose_name='Специализация')
   education = models.CharField(max_length=120, choices=education_types, verbose_name='Образование')
   sex = models.CharField(max_length=120, choices=sex_types, verbose_name='Пол')
   date_of_birth = models.DateField(verbose_name='День рождения')
   date_of_start = models.DateField(verbose_name='День начала работы в клинике')
   date_of_end = models.DateField(verbose_name='День конца работы в клинике', blank=True, null=True)
   contract = models.CharField(max_length=120, verbose_name='Данные по договору')
   # schedule = models.ManyToManyField('Schedule', verbose_name='График работы', through='ScheduleOfDoctor',
   #                                   related_name='doctor_schedule', blank=True, default=None)
   # schedule = models.ForeignKey('ScheduleOfDoctor', on_delete=models.CASCADE, verbose_name='График работы', blank=True, default=None)

   def __str__(self):
      return self.first_name + " " + self.last_name + " / " + str(self.specialization)


class ScheduleOfDoctor(models.Model):
   # schedule = models.ForeignKey('Schedule', verbose_name='Расписание', on_delete=models.CASCADE, blank=True)
   weekday = models.CharField(max_length=120, choices=weekdays, verbose_name='День недели', blank=True, default=None)
   doctor = models.ForeignKey('Doctor', verbose_name='Доктор', on_delete=models.CASCADE)
   # status = models.BooleanField(verbose_name='Работает', default=0)


class Cabinet(models.Model):
   number = models.IntegerField(verbose_name='Номер кабинета', default=0)
   # schedule = models.ForeignKey('ScheduleOfCabinet', on_delete=models.CASCADE, verbose_name='График работы', blank=True,
   #                              default=None)
   # schedule = models.ManyToManyField('Schedule', verbose_name='График работы', through='ScheduleOfCabinet',
   #                                   related_name='cabinet_schedule')
   cabinet_officer = models.ForeignKey('CabinetOfficer', on_delete=models.CASCADE, verbose_name='Ответственный за кабинет')
   phone_number = models.IntegerField(verbose_name='Внутренний телефон', default=0)

   def __str__(self):
      return str(self.number)


class CabinetOfficer(models.Model):
   first_name = models.CharField(max_length=120, verbose_name='Имя')
   last_name = models.CharField(max_length=120, verbose_name='Фамилия')

   def __str__(self):
      return self.first_name + " " + self.last_name


class ScheduleOfCabinet(models.Model):
   weekday = models.CharField(max_length=120, choices=weekdays, verbose_name='День недели', blank=True, default=None)
   # schedule = models.ForeignKey('Schedule', verbose_name='Расписание', on_delete=models.CASCADE)
   cabinet = models.ForeignKey('Cabinet', verbose_name='Кабинет', on_delete=models.CASCADE)
   # status = models.BinaryField(verbose_name='Статус', default=0)


class PriceList(models.Model):
   service = models.CharField(max_length=120, verbose_name='Название услуги')
   price = models.IntegerField(verbose_name='Цена', default=0)

   def __str__(self):
      return self.service


class Visit(models.Model):
   date = models.DateField(verbose_name='Дата приема', default=datetime.date.today)
   doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, verbose_name='Доктор')
   patient = models.ForeignKey('Patient', on_delete=models.CASCADE, verbose_name='Пациент')
   diagnose = models.CharField(max_length=120, verbose_name='Диагноз')
   current_status = models.TextField(verbose_name='Текущее состояние больного')
   recommendation = models.TextField(verbose_name='Рекомендации по лечению')
   cabinet = models.ForeignKey('Cabinet', on_delete=models.CASCADE, verbose_name='Кабинет')
   price = models.ForeignKey('PriceList', on_delete=models.CASCADE, verbose_name='Цена')

   def __str__(self):
      return str(self.doctor) + " / " + str(self.date)


# class VisitOfPatient(models.Model):
#    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, verbose_name='Пациент')
#    visit = models.ForeignKey('Visit', on_delete=models.CASCADE, verbose_name = 'График работы')
#    medical_card = models.ForeignKey('MedicalCard', on_delete=models.CASCADE, verbose_name='Мед карта')


class MedicalCard(models.Model):
   patient = models.ForeignKey('Patient', on_delete=models.CASCADE, verbose_name='Пациент')
   # visit = models.ManyToManyField('Visit', verbose_name = 'График работы', through='VisitOfPatient', related_name = 'visit_of_patient')
   visit = models.ForeignKey('Visit', on_delete=models.CASCADE, verbose_name = 'Визит', default=0, blank=True)

   def __str__(self):
      return str(self.visit)
