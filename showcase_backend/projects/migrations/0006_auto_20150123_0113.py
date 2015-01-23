# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150121_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.FileField(upload_to=b'screenshot/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
