# Generated by Django 3.2.8 on 2021-11-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='number',
            field=models.CharField(default='o 000 oo', max_length=15),
            preserve_default=False,
        ),
    ]