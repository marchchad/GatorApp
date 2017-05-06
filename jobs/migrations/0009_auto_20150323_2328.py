# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20150323_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imgBytes',
        ),
        migrations.AddField(
            model_name='image',
            name='imgFile',
            field=models.FileField(default='', upload_to='job/'),
            preserve_default=False,
        ),
    ]
