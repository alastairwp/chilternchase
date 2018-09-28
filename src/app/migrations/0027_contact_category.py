# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_remove_contact_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ContactCategory'),
        ),
    ]