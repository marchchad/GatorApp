# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20150323_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('data', models.BinaryField()),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('public', models.BooleanField(default=True)),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
