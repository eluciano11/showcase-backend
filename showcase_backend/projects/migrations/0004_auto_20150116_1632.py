# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_auto_20150113_2041'),
        ('departments', '0003_department_slug'),
        ('projects', '0003_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='department',
            field=models.ForeignKey(to='departments.Department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='university',
            field=models.ForeignKey(to='universities.University'),
            preserve_default=False,
        ),
    ]
