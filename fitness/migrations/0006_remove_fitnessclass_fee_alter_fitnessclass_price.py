# Generated by Django 5.1.3 on 2024-11-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_merge_20241130_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessclass',
            name='fee',
        ),
        migrations.AlterField(
            model_name='fitnessclass',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]