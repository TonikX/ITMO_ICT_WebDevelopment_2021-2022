# Generated by Django 3.2.9 on 2021-12-12 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gos_num', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birthdate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('ex_date', models.DateField()),
                ('car_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField()),
                ('end', models.DateField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('car_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
    ]
