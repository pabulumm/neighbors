# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('neighborhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('family_name', models.CharField(default=b'family_name', max_length=50)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('address', models.CharField(default=b'Unknown', max_length=100)),
                ('neighborhood', models.ForeignKey(to='neighborhood.Neighborhood')),
            ],
        ),
    ]
