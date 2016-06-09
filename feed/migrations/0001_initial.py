# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '__first__'),
        ('polls', '__first__'),
        ('neighborhood', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('neighborhood', models.ForeignKey(to='neighborhood.Neighborhood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, default='ANNOUNCEMENT')),
                ('text', models.TextField(max_length=1000)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('decision', models.ForeignKey(null=True, to='polls.Poll')),
                ('feed', models.ForeignKey(null=True, to='feed.Feed')),
                ('marker', models.ForeignKey(null=True, to='markers.Marker')),
                ('poll', models.ForeignKey(null=True, to='polls.Question')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(to='feed.FeedPost')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
