# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_poll_votepoll'),
        ('feed', '0010_auto_20160417_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedpost',
            name='decision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AlterField(
            model_name='feedpost',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
