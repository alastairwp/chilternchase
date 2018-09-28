# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20180123_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='logo_url',
            field=models.ImageField(blank=True, null=True, upload_to='admin_file_uploads'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='registered_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Registered number'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter URL'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='amount_raised',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount raised'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='cover_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='admin_file_uploads'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='long_description',
            field=models.TextField(blank=True, null=True, verbose_name='Long description'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='race_year',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='admin_file_uploads'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cc_contact',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CC Contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='organisation',
            field=models.CharField(blank=True, max_length=255, verbose_name='Organisation'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='contactcategory',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=255, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='email_address',
            field=models.CharField(max_length=255, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='marketingsource',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='marketingsource',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='nvp',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='nvp',
            name='value',
            field=models.CharField(max_length=255, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='entrant_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Entrant number'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='extension',
            field=models.CharField(max_length=4, verbose_name='File extensions'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='filename',
            field=models.CharField(max_length=100, verbose_name='Filename'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='race_year',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url_pre_string',
            field=models.CharField(max_length=255, verbose_name='URL pre-string'),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_year',
            field=models.PositiveIntegerField(verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='result',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='result',
            name='chip_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Chip time'),
        ),
        migrations.AlterField(
            model_name='result',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='result',
            name='entrant_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Entrant number'),
        ),
        migrations.AlterField(
            model_name='result',
            name='finish_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Finish time'),
        ),
        migrations.AlterField(
            model_name='result',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='Firstname'),
        ),
        migrations.AlterField(
            model_name='result',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='result',
            name='no_mail',
            field=models.BooleanField(default=False, verbose_name='No mail'),
        ),
        migrations.AlterField(
            model_name='result',
            name='performance_grading',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Performance grading'),
        ),
        migrations.AlterField(
            model_name='result',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='result',
            name='race_type',
            field=models.CharField(max_length=10, verbose_name='Race type'),
        ),
        migrations.AlterField(
            model_name='result',
            name='race_year',
            field=models.PositiveIntegerField(default=0, verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='result',
            name='registration_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Registration number'),
        ),
        migrations.AlterField(
            model_name='result',
            name='split_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Split time'),
        ),
        migrations.AlterField(
            model_name='result',
            name='surname',
            field=models.CharField(max_length=255, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='result',
            name='team_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Team name'),
        ),
        migrations.AlterField(
            model_name='runningclub',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='runningclub',
            name='logo_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Logo URL'),
        ),
        migrations.AlterField(
            model_name='runningclub',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='runningclub',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Logo URL'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='message',
            field=models.CharField(max_length=1000, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='previous_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Previous name'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='race_year',
            field=models.PositiveIntegerField(default=0, verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='terms_agreed',
            field=models.DateTimeField(verbose_name='Terms agreed'),
        ),
    ]
