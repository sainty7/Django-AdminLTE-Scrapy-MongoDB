# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0006_auto_20151119_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='content',
        ),
        migrations.RemoveField(
            model_name='file',
            name='files',
        ),
        migrations.AddField(
            model_name='file',
            name='note',
            field=models.CharField(default=datetime.datetime(2015, 11, 22, 8, 53, 31, 288106, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
