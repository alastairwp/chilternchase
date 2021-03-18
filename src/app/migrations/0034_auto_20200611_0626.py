# Generated by Django 3.0.6 on 2020-06-11 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20191008_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketingsource',
            name='marketingsource_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='marketingsource_id',
        ),
        migrations.AddField(
            model_name='marketingsource',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marketing_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.MarketingSource'),
        ),
    ]