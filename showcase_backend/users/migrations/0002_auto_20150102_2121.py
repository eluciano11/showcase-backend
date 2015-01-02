# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('universities', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=b'1', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('department', models.ForeignKey(to='departments.Department')),
                ('university', models.ForeignKey(to='universities.University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university',
        ),
        migrations.AlterField(
            model_name='user',
            name='token_version',
            field=models.CharField(default=b'6564d4e5-ccbe-4203-89eb-786bbb49fc63', unique=True, max_length=36, db_index=True),
            preserve_default=True,
        ),
    ]
