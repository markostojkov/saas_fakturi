# Generated by Django 2.2.2 on 2020-01-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_invoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(max_length=15),
        ),
    ]
