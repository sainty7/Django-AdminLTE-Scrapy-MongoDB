# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0008_person_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo',
        ),
        migrations.AddField(
            model_name='person',
            name='photo_url',
            field=models.FileField(default=datetime.datetime(2015, 11, 23, 13, 50, 38, 729494, tzinfo=utc), upload_to=b'/user'),
            preserve_default=False,
        ),
    ]
