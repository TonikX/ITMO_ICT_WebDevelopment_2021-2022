# Generated by Django 3.0.6 on 2020-10-07 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201007_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
    ]
