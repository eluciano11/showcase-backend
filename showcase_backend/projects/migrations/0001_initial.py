# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150102_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('story', models.TextField()),
                ('screenshot', models.FileField(upload_to=b'screenshot/%Y/%m/%d')),
                ('created_by', models.ForeignKey(to='users.User')),
            ],
            options={
                'ordering': ['created_at'],
            },
            bases=(models.Model,),
        ),
    ]
