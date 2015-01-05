# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 20, 56, 17, 212648), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'a50025ab-8ec2-4c9a-a27e-77aa78b1f769', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
