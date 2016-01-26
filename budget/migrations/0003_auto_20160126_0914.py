# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20160126_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='budget',
        ),
        migrations.AddField(
            model_name='budget',
            name='neighborhood_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='budget_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
