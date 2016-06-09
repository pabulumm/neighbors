# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(verbose_name='Comment Text')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=250, default='Discussion Title', verbose_name='Discussion Title')),
                ('description', models.TextField(default='Initial presentation of the Discussion Topic', verbose_name='Discussion Description')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('neighborhood', models.ForeignKey(to='neighborhood.Neighborhood', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(to='discussions.Discussion', null=True),
            preserve_default=True,
        ),
    ]
