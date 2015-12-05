# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0002_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='files',
            field=models.FileField(default=1, upload_to=b'./upload/'),
            preserve_default=False,
        ),
    ]
