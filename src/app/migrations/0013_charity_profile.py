# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_charity_amount_raised'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity_Profile',
            fields=[
                ('charity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('registered_number', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Registered number')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name=b'Short description')),
                ('long_description', models.TextField(blank=True, null=True, verbose_name=b'Long description')),
                ('enabled', models.BooleanField(default=False, verbose_name=b'Enabled')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Website URL')),
                ('logo_url', models.ImageField(blank=True, null=True, upload_to=b'admin_file_uploads')),
                ('cover_image_url', models.ImageField(blank=True, null=True, upload_to=b'admin_file_uploads')),
                ('video_url', models.FileField(blank=True, null=True, upload_to=b'admin_file_uploads')),
                ('order', models.PositiveIntegerField(default=0, verbose_name=b'Order')),
                ('race_years', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Race years')),
                ('amount_raised', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Amount raised')),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Facebook URL')),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Twitter URL')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
