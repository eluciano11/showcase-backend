# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20150111_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='slug',
            field=models.SlugField(default=' ', unique=True),
            preserve_default=False,
        ),
    ]
