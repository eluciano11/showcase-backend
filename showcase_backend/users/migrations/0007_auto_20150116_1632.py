# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150113_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university',
        ),
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'f226f1f3-916e-4d58-b47c-bb73937fcec0', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
