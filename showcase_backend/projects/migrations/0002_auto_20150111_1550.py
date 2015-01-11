# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.CharField(default=' ', max_length=140),
            preserve_default=False,
        ),
    ]
