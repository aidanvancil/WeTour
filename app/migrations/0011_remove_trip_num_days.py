# Generated by Django 4.2 on 2023-04-23 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_trip_description_remove_trip_tour_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='num_days',
        ),
    ]
