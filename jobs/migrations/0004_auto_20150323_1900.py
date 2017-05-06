# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150323_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='share_job',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='share_location',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
