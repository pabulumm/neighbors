# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=400)),
                ('description', models.TextField(default='Default question description', max_length=1000)),
                ('status', models.CharField(default='TBD', max_length=20)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(null=True, to='neighborhood.Neighborhood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('description', models.TextField(default='Default question description', max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=django.utils.timezone.now)),
                ('is_yes_no', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(null=True, to='neighborhood.Neighborhood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('choice', models.ForeignKey(null=True, to='polls.Choice')),
                ('question', models.ForeignKey(null=True, to='polls.Question')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotePoll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
                ('poll', models.ForeignKey(null=True, to='polls.Poll')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'choice')]),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, to='polls.Question'),
            preserve_default=True,
        ),
    ]
