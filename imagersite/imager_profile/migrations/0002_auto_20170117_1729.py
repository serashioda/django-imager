# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerprofile',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]