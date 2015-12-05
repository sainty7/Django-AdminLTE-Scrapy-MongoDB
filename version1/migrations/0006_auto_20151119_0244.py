# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0005_auto_20151117_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.CharField(default=20151119, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(upload_to=b'/home/mtbf3/'),
            preserve_default=True,
        ),
    ]
