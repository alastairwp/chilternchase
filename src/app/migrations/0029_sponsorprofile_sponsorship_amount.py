# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20180514_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorprofile',
            name='sponsorship_amount',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Sponsorship Amount'),
        ),
    ]