# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150116_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'11e9749b-0851-4b23-abfa-2f0b37ef959c', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
