# Generated by Django 3.2.9 on 2021-11-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]