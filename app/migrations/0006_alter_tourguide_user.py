# Generated by Django 4.2 on 2023-04-23 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_alter_tourguide_user_alter_trip_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourguide',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]
