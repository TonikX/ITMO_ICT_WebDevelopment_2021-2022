# Generated by Django 4.0 on 2021-12-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_cod', models.IntegerField(verbose_name='код города')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('coord_lon', models.FloatField()),
                ('coord_lat', models.FloatField()),
            ],
        ),
    ]
