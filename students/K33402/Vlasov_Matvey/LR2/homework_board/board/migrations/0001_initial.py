# Generated by Django 3.2.8 on 2021-10-27 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.teacher')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.discipline')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('class_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.class')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.discipline')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.teacher')),
            ],
            options={
                'unique_together': {('class_school', 'discipline')},
            },
        ),
        migrations.AddField(
            model_name='class',
            name='disciplines',
            field=models.ManyToManyField(through='board.ClassDiscipline', to='board.Discipline'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('solution', models.CharField(blank=True, max_length=500)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('grade', models.IntegerField(blank=True, choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2')], null=True)),
                ('grade_comment', models.CharField(blank=True, max_length=500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.task')),
            ],
        ),
    ]
