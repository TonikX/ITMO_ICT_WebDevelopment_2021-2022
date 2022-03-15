# Generated by Django 3.2.8 on 2021-10-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_auto_20211030_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_owner',
            name='infor',
        ),
        migrations.AddField(
            model_name='car_owner',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='car_owner',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='car_owner',
            name='passport',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
