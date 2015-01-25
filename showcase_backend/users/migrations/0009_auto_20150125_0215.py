# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150120_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'585f66e0-eb73-40ec-b054-7a49cc6b0b23', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
