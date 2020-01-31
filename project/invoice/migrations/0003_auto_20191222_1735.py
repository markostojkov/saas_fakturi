# Generated by Django 2.2.2 on 2019-12-22 16:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20191222_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid_sum',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=''),
        ),
    ]