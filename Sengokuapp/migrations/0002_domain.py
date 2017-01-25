# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sengokuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('photo', models.URLField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('近畿', '近畿'), ('东海道', '东海道'), ('东山道', '东山道'), ('北陆道', '北陆道'), ('山阴道', '山阴道'), ('山阳道', '山阳道'), ('南海道', '南海道'), ('西海道', '西海道')], max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
