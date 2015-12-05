# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0009_auto_20151123_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo_url',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
