# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='has_budget',
            field=models.BooleanField(default=False),
        ),
    ]
