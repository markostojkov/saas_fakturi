# Generated by Django 2.2.2 on 2020-01-13 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('payments', '0002_auto_20191227_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
        ),
    ]
