# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20180122_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Position')),
                ('organisation', models.CharField(blank=True, max_length=255, verbose_name=b'Organisation')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name=b'Email')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name=b'Website')),
                ('telephone', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Telephone')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Mobile')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Address')),
                ('cc_contact', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'CC Contact')),
            ],
        ),
        migrations.CreateModel(
            name='ContactCategory',
            fields=[
                ('contact_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ContactCategory'),
        ),
    ]