# Generated by Django 3.2.8 on 2021-10-30 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_owner',
            name='infor',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='adrress',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
