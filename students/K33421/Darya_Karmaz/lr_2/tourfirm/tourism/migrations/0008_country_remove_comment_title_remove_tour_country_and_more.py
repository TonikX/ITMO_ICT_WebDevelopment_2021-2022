# Generated by Django 4.0 on 2021-12-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0007_comment_beginning_date_comment_ending_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='country',
        ),
        migrations.AddField(
            model_name='tour',
            name='country',
            field=models.ManyToManyField(to='tourism.Country'),
        ),
    ]
