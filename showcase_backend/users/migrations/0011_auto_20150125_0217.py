# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150125_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'1d0db7eb-997a-4840-b7f3-d392233d3b75', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
