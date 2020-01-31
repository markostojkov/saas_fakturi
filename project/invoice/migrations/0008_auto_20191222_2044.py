# Generated by Django 2.2.2 on 2019-12-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('invoice', '0007_invoice_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid_sum',
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid_sum',
            field=models.ManyToManyField(to='payments.Payment'),
        ),
    ]