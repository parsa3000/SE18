# Generated by Django 2.0.2 on 2018-04-29 03:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180428_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='trophies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=8),
        ),
    ]
