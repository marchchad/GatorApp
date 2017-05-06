# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('current', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('start_date', models.DateTimeField(verbose_name='Contract Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Contract End Date')),
                ('agreement_date', models.DateTimeField(verbose_name='Date Signed')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('desc', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('start_date', models.DateTimeField(verbose_name='Job Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Job End Date')),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('estimated_cost', models.FloatField(verbose_name='Estimate')),
                ('current_cost', models.FloatField(verbose_name='Current Cost')),
                ('final_cost', models.FloatField(verbose_name='Final Cost')),
                ('location_addr', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('mat_type', models.CharField(max_length=100)),
                ('count', models.FloatField()),
                ('weight', models.FloatField()),
                ('weight_unit', models.CharField(max_length=3)),
                ('cost_per_unit', models.FloatField(verbose_name='Cost per unit')),
                ('cost_per_weight', models.FloatField(verbose_name='Cost per weight')),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contract',
            name='job',
            field=models.ForeignKey(to='jobs.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='job',
            field=models.ForeignKey(to='jobs.Job'),
            preserve_default=True,
        ),
    ]
