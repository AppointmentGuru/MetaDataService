# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-10 21:09
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_jsonblob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='owner',
        ),
        migrations.AddField(
            model_name='note',
            name='owners',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=[], size=None),
        ),
    ]