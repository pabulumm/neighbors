# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_of_marker', models.CharField(max_length=40, default='DEFAULT')),
                ('description', models.TextField(max_length=300, default='Default marker description.')),
                ('neighborhood_id', models.IntegerField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
