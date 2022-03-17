from django.db import models
# Create your models here.


class Book(models.Model):
    """ Описание книги """
    name = models.CharField(max_length=200, verbose_name='Название книги')
    authors  = models.CharField(max_length=500, verbose_name='Автор(ы)')
    publisher = models.CharField(max_length=200, verbose_name='Издательство')
    pub_year = models.DateField(verbose_name='Год публикации')
    section = models.CharField(max_length=20, verbose_name='Раздел')
    instance_count = models.IntegerField(verbose_name='Количество экземпляров в библиотеке')
    bk_cipher = models.CharField(max_length=10, verbose_name='Шифр книги')

    def __str__(self):
        return "{} by {}.".format(self.name, self.authors)
class Halls(models.Model):
    hall_num = models.IntegerField(verbose_name='Номер зала')
    hall_name = models.CharField(max_length=300, verbose_name='Название зала')
    capacity = models.IntegerField(verbose_name='Вместимость')
    
    def __str__(self):
        return self.hall_name

class Readers(models.Model):
    educ_choice = (
        ('b', 'начальное'), 
        ('m', 'среднее'),
        ('h', 'высшее')
    )
    s_choice = (
        ('1', 'есть'),
        ('0', 'нет')
    )
    reader_ticket_number = models.IntegerField(verbose_name='Номер читательского билета')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    passport = models.CharField(max_length=10, verbose_name='Номер паспорта', unique=True)
    birth_date = models.DateField(verbose_name='Дата рождения')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Номер телефона')
    education = models.CharField(max_length=1, choices=educ_choice, verbose_name='Образование')
    scientist = models.CharField(max_length=1, choices=s_choice, verbose_name='Наличие ученной степени')
    attached_books = models.ManyToManyField('Book', through='BookAttachment', 
    verbose_name='Закрепленные книги', blank=True)
    hall = models.ManyToManyField('Halls', through='ReaderAttachment', verbose_name='Зал', blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class BookAttachment(models.Model):
    attach_date = models.DateTimeField(verbose_name='Дата закрепления')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, verbose_name='Название книги')
    reader = models.ForeignKey("Readers", on_delete=models.CASCADE, verbose_name="ФИО читателя")

class ReaderAttachment(models.Model):
    attach_date = models.DateTimeField(verbose_name='Дата закрепления читателя')
    reader = models.ForeignKey("Readers", on_delete=models.CASCADE, verbose_name='ФИО читателя')
    hall = models.ForeignKey("Halls", on_delete=models.CASCADE, verbose_name='Название зала')

