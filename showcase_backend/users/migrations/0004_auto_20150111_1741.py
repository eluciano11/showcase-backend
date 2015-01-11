# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150104_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'1aa4502c-a866-481b-80da-a6d7fa58de76', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
