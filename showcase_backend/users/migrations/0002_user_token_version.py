# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'a7adea63-2d9e-40ff-bc1d-141cb61b3a26', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
