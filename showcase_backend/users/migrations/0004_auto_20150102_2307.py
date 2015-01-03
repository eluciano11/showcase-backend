# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150102_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'517a1f7b-c772-4ca1-a4a3-3cdc8835b4c3', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
