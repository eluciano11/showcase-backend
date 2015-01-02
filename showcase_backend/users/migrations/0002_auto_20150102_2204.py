# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'4b9febd8-a744-43b2-80eb-d12f318ce50a', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
