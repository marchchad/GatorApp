# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150323_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image_count',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='image_name_base',
            field=models.CharField(max_length=50, default='a'),
            preserve_default=False,
        ),
    ]
