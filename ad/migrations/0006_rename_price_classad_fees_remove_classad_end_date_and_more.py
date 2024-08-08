# Generated by Django 5.0.7 on 2024-08-07 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_classad_end_date_classad_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classad',
            old_name='price',
            new_name='fees',
        ),
        migrations.RemoveField(
            model_name='classad',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='classad',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='rentalad',
            name='location',
        ),
        migrations.RemoveField(
            model_name='rentalad',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='salead',
            name='email',
        ),
        migrations.RemoveField(
            model_name='salead',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='salead',
            name='show_email',
        ),
        migrations.RemoveField(
            model_name='salead',
            name='show_phone',
        ),
        migrations.AddField(
            model_name='eventad',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='eventad',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]