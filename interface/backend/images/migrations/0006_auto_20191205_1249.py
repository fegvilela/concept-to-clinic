# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-12-05 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_remove_imagelocation_series'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagefile',
            options={'ordering': ('slice_location',)},
        ),
    ]