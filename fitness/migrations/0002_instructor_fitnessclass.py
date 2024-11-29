# Generated by Django 5.1.3 on 2024-11-29 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Pilates', 'Pilates'), ('Aqua Aerobics', 'Aqua Aerobics'), ('Cardio', 'Cardio'), ('Zumba', 'Zumba')], max_length=100)),
                ('duration', models.DurationField()),
                ('capacity', models.IntegerField(default=15)),
                ('booked', models.IntegerField(default=0)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.instructor')),
            ],
        ),
    ]
