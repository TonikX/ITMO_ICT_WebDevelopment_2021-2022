# Generated by Django 3.2.10 on 2021-12-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0009_auto_20211222_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
    ]
