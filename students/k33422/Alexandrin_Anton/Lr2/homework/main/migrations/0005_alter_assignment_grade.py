# Generated by Django 3.2.9 on 2021-11-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211110_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='grade',
            field=models.CharField(blank=True, default='-', max_length=5),
        ),
    ]
