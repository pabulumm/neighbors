# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-26 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20160326_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedpost',
            name='feed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.Feed'),
        ),
    ]
