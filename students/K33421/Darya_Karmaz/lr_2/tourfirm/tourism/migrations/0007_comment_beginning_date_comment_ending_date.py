# Generated by Django 4.0 on 2021-12-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0006_alter_tourist_first_name_alter_tourist_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='beginning_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='ending_date',
            field=models.DateField(null=True),
        ),
    ]
