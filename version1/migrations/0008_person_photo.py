# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0007_auto_20151122_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2015, 11, 23, 12, 57, 13, 400844, tzinfo=utc), upload_to=b'users'),
            preserve_default=False,
        ),
    ]
