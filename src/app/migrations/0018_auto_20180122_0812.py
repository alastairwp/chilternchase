# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20180122_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charityprofile',
            name='charity_profile_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
