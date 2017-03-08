# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 06:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('published', models.CharField(choices=[('public', 'public'), ('shared', 'shared'), ('private', 'private')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover_photo', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='album_photo', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]