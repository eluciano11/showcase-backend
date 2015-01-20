# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150116_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.FileField(upload_to=b'screenshot/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
