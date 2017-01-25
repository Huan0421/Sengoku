# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sengokuapp', '0002_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('photo', models.URLField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('jj', 'jj'), ('dhd', 'dhd'), ('dsd', 'dsd'), ('bld', 'bld'), ('syd', 'syd'), ('syd', 'syd'), ('nhd', 'nhd'), ('xhd', 'xhd')], max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='domain',
            name='gender',
            field=models.CharField(blank=True, choices=[('jj', 'jj'), ('dhd', 'dhd'), ('dsd', 'dsd'), ('bld', 'bld'), ('syd', 'syd'), ('syd', 'syd'), ('nhd', 'nhd'), ('xhd', 'xhd')], max_length=200, null=True),
        ),
    ]