# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150113_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'7f11e24e-1f0c-49b4-8ded-209e900c1805', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
