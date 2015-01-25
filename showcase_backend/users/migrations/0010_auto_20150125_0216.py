# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150125_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'5fae9d8a-de34-4cc9-82fe-4a55513405a8', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
