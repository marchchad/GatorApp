# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 5, 26, 31, 62123, tzinfo=utc), verbose_name='Date Added'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.BinaryField(verbose_name='Image Data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.CharField(max_length=300, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Is Visible to Public?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
