# Generated by Django 3.2.9 on 2021-11-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20211108_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]