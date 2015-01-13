# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150111_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=b'hello', unique=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'57d3e908-28fd-47ae-a5c8-acd278c665f9', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
