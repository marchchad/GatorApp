# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField(verbose_name='Content')),
                ('pub_date', models.DateField(verbose_name='Added On')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Inspection')),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('inspector', models.CharField(max_length=50, verbose_name='Inspector')),
                ('inspection_date', models.DateField(verbose_name='Inspection Date')),
                ('initial_inspection', models.BooleanField(default=True)),
                ('was_rescheduled', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('permit_type', models.CharField(max_length=100, verbose_name='Permit')),
                ('number', models.IntegerField(verbose_name='Permit #')),
                ('agency', models.CharField(max_length=200, verbose_name='Permitted By')),
                ('issue_date', models.DateField(verbose_name='Date Issued')),
                ('valid_on', models.DateField(verbose_name='Valid On')),
                ('expires_on', models.DateField(verbose_name='Expires On')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='fname',
            field=models.CharField(max_length=50, verbose_name='First name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='lname',
            field=models.CharField(max_length=50, verbose_name='Last name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='location_addr',
            field=models.CharField(max_length=200, verbose_name='Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='count',
            field=models.FloatField(verbose_name='Count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='mat_type',
            field=models.CharField(max_length=100, verbose_name='Material'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='weight',
            field=models.FloatField(verbose_name='Weight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='weight_unit',
            field=models.CharField(max_length=3, verbose_name='Unit'),
            preserve_default=True,
        ),
    ]
