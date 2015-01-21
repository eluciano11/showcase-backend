# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
    ]
