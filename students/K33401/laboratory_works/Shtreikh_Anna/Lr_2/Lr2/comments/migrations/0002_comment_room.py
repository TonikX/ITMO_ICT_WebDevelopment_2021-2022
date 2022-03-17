# Generated by Django 3.2.9 on 2022-01-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room'),
        ),
    ]