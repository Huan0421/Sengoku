# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sengokuapp', '0007_road_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='component',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='family',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='product',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='scenic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='domain',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
