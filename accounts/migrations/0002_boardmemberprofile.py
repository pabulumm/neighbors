# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-24 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('neighborhood', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMemberProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bio', models.CharField(max_length=400)),
                ('position', models.CharField(max_length=50, verbose_name='Board member position')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighborhood.House')),
            ],
        ),
    ]
