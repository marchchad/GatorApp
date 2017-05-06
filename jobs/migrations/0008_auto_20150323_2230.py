# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20150323_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='data',
            new_name='imgBytes',
        ),
    ]
