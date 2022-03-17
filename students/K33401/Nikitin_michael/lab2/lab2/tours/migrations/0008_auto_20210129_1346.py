# Generated by Django 3.1.5 on 2021-01-29 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_remove_userscomments_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userscomments',
            name='commenting_user',
        ),
        migrations.RemoveField(
            model_name='userscomments',
            name='tour',
        ),
        migrations.AddField(
            model_name='userscomments',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tours.booked'),
            preserve_default=False,
        ),
    ]
