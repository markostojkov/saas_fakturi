# Generated by Django 2.2.2 on 2019-12-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20191222_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_number',
            new_name='slug',
        ),
    ]