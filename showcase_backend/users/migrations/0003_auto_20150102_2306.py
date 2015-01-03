# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150102_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'208f5b71-4dbd-4409-81b8-3c8acd309a54', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
