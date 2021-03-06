# Generated by Django 3.2.8 on 2021-12-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='card_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Читательский билет'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='degree',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Ученая степень'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='education',
            field=models.CharField(blank=True, choices=[('Среднее общее', 'Среднее общее'), ('Среднее специальное', 'Среднее специальное'), ('Высшее', 'Высшее'), ('Неоконченное высшее', 'Неоконченное высшее'), ('Неоконченное среднее', 'Неоконченное среднее')], default='-', max_length=500, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='passport',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Телефон'),
        ),
    ]
