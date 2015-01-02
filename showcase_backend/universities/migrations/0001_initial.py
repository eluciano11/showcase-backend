# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('emblem', models.FileField(upload_to=b'emblems/%Y/%m/%d')),
                ('town', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name', 'town'],
                'verbose_name_plural': 'universities',
            },
            bases=(models.Model,),
        ),
    ]
