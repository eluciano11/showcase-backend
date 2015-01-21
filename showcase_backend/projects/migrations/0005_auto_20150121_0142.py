# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150116_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
    ]
