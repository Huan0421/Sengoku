# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-28 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sengokuapp', '0018_family_photo_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='photo_add',
        ),
    ]
