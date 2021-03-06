# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 17:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0023_auto_20180125_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceSponsor',
            fields=[
                ('sponsor_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorProfile',
            fields=[
                ('sponsor_profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('enabled', models.BooleanField(default=False, verbose_name=b'Enabled')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Website URL')),
                ('logo_url', models.ImageField(blank=True, null=True, upload_to=b'media')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Marketing',
            new_name='MarketingPreference',
        ),
        migrations.RenameModel(
            old_name='NVP',
            new_name='Setting',
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
        migrations.AlterModelOptions(
            name='marketingpreference',
            options={'verbose_name_plural': 'Marketing Preferences'},
        ),
        migrations.RenameField(
            model_name='charityprofile',
            old_name='charity_id',
            new_name='charity',
        ),
        migrations.RenameField(
            model_name='contactcategory',
            old_name='contact_category_id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='marketing_id',
            new_name='marketing_preference_id',
        ),
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='runningclub',
            old_name='runningclub_id',
            new_name='running_club_id',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='nvp_id',
            new_name='setting_id',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='userprofile_id',
            new_name='user_profile_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='race_id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='race_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ContactCategory'),
        ),
        migrations.AddField(
            model_name='photo',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Race'),
        ),
        migrations.AddField(
            model_name='result',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Race'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='marketing_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.MarketingSource'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='cover_image_url',
            field=models.ImageField(blank=True, null=True, upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_year',
            field=models.CharField(max_length=10, verbose_name=b'Race year'),
        ),
        migrations.AddField(
            model_name='userphoto',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Photo'),
        ),
        migrations.AddField(
            model_name='userphoto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='racesponsor',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Race'),
        ),
        migrations.AddField(
            model_name='racesponsor',
            name='sponsor_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SponsorProfile'),
        ),
    ]
