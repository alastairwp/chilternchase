# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='race_id',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name=b'Race Id'),
        ),
    ]
