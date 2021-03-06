# Generated by Django 4.0 on 2021-12-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('beginning_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('country', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('agency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.agency')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.tour')),
                ('tourist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.tourist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('rate', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], max_length=30)),
                ('tour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.tour')),
                ('tourist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.tourist')),
            ],
        ),
    ]
