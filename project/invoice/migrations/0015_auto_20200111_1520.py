# Generated by Django 2.2.2 on 2020-01-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0014_auto_20200111_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='slug',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
