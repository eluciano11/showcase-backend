# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.URLField(default='hello'),
            preserve_default=False,
        ),
    ]
