# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0003_auto_20170119_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerprofile',
            name='active',
        ),
    ]
