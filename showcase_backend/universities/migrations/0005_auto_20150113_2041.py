# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0004_auto_20150111_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=b'hello', unique=True, editable=False),
            preserve_default=True,
        ),
    ]
