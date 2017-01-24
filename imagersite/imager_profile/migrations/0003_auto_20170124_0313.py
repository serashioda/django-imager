# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_auto_20170117_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera_type',
            field=models.CharField(choices=[('CANNON', 'Cannon'), ('IPHONE', 'iPhone'), ('NIKON', 'Nikon'), ('POLAROID', 'polaroid')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photo_type',
            field=models.CharField(choices=[('LANDSCAPE', 'Landscape'), ('PORTRAIT', 'Portrait'), ('BLACK_WHITE', 'Black and White')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='travel_radius',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
