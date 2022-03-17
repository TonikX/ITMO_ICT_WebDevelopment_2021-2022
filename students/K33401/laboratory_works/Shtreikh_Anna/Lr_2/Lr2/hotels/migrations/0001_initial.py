# Generated by Django 3.2.9 on 2022-01-13 12:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('1R', 'One room'), ('2R', 'Two rooms'), ('3R', 'Three rooms'), ('LUX', 'Lux')], max_length=50)),
                ('cost', models.FloatField()),
                ('bulk', models.FloatField()),
                ('comfort', models.CharField(blank=True, max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.DateTimeField()),
                ('departure', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
            ],
        ),
    ]