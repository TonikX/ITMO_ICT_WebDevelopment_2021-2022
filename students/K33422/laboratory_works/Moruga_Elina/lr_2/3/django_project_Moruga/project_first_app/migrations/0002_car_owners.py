# Generated by Django 3.2.8 on 2021-11-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.CarOwner'),
        ),
    ]
