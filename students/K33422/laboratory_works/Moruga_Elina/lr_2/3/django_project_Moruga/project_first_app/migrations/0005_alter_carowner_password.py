# Generated by Django 3.2.8 on 2021-11-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_auto_20211104_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
