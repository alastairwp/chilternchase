# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20180530_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorprofile',
            name='logo_url',
            field=models.ImageField(blank=True, null=True, upload_to=b'uploads/'),
        ),
    ]
