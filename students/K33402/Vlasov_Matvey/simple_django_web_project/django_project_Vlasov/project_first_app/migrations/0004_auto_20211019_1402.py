# Generated by Django 3.2.8 on 2021-10-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20211019_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owneruser',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='owneruser',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
