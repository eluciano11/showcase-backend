# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_university_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='university',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
    ]
