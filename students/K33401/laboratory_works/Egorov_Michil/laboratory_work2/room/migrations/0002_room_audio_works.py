# Generated by Django 3.1.4 on 2020-12-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='audio_works',
            field=models.BooleanField(default=False),
        ),
    ]
