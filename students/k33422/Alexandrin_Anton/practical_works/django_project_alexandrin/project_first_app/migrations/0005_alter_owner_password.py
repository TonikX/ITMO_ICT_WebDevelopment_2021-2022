# Generated by Django 3.2.9 on 2021-11-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_auto_20211108_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='password',
            field=models.CharField(default='123', max_length=20),
        ),
    ]
