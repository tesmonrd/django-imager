# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 03:07
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
        migrations.AddField(
            model_name='album',
            name='photographer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='ablums',
            field=models.ManyToManyField(related_name='photos', to='imager_images.Album'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photographer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
        ),
    ]