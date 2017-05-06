# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150323_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Added On'),
            preserve_default=True,
        ),
    ]
