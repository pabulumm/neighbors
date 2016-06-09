# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '__first__'),
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('activity_type', models.CharField(max_length=30, default='POST')),
                ('assoc_obj_id', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('bio', models.TextField(max_length=1000, default='Default biography')),
                ('member_status', models.CharField(max_length=100, default='neighbor')),
                ('neighborhood_id', models.IntegerField(null=True)),
                ('house', models.ForeignKey(null=True, to='neighborhood.House')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
