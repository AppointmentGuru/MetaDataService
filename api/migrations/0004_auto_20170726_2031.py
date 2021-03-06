# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 20:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170726_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='imagedocument',
            name='owner',
        ),
        migrations.AddField(
            model_name='document',
            name='owners',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=[], size=None),
        ),
        migrations.AddField(
            model_name='imagedocument',
            name='owners',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='object_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=[], size=None),
        ),
    ]
