# Generated by Django 2.2.2 on 2020-01-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0016_auto_20200111_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='full_sum',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax_sum',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
