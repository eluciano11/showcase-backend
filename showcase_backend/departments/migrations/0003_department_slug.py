# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20150104_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=' ', editable=False),
            preserve_default=False,
        ),
    ]
