# Generated by Django 4.0 on 2022-01-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0002_alter_scheduleofcabinet_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleofcabinet',
            name='status',
        ),
        migrations.RemoveField(
            model_name='scheduleofdoctor',
            name='status',
        ),
    ]
