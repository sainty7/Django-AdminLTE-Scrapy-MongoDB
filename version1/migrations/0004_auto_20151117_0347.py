# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0003_file_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='files',
            field=models.FileField(upload_to=b'uploads'),
            preserve_default=True,
        ),
    ]
