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
            field=models.CharField(default=b'0120399f-7079-4c46-822f-1c3aaa5e5c84', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
