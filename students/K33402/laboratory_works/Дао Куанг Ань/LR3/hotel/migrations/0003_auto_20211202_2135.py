# Generated by Django 3.2.9 on 2021-12-02 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20211202_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floor',
            name='id_room',
        ),
        migrations.AddField(
            model_name='room',
            name='id_floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.floor'),
        ),
    ]
