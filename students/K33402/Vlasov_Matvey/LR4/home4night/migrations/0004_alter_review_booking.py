# Generated by Django 4.0 on 2021-12-10 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home4night', '0003_alter_review_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home4night.booking'),
        ),
    ]
