# Generated by Django 3.2.9 on 2021-11-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_remove_invoice_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='pdf_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
