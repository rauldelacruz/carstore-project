# Generated by Django 3.1.5 on 2021-02-11 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_car_drivetrain_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='drivetrain_choices',
            new_name='drivetrain',
        ),
    ]