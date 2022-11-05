# Generated by Django 3.2.9 on 2022-01-14 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_reservation_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0005_auto_20220114_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
