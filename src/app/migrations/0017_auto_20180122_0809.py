# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20180122_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charityprofile',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
