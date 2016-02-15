# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20160211_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='approval_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
