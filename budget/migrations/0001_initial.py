# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Budget Title', default='Community Budget', max_length=60)),
                ('total_funds', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Total Funds', default=0.0)),
                ('total_expenses', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Total Expenses', default=0.0)),
                ('residence_fee', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Residence Fee', default=10.0)),
                ('create_date', models.DateTimeField(verbose_name='Created on', default=django.utils.timezone.now)),
                ('neighborhood', models.ForeignKey(to='neighborhood.Neighborhood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('types', models.CharField(choices=[('IMP', 'Improvement'), ('REP', 'Repair'), ('REC', 'Recreation'), ('FEE', 'Fee'), ('OTH', 'Other')], default='REP', max_length=3)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Expense Title', default='Expense', max_length=60)),
                ('description', models.TextField(verbose_name='Description', default='Description of why and how this expense is needed')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('create_date', models.DateTimeField(verbose_name='Created on', default=django.utils.timezone.now)),
                ('start_date', models.DateTimeField(verbose_name='Starts on')),
                ('end_date', models.DateTimeField(verbose_name='Ends on')),
                ('type', models.CharField(verbose_name='Type of Expense', max_length=50)),
                ('approved', models.BooleanField(default=False)),
                ('budget', models.ForeignKey(to='budget.Budget')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
