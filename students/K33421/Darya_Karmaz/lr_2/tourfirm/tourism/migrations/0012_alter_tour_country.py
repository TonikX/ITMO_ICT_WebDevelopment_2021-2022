# Generated by Django 4.0 on 2021-12-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0011_alter_tour_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
