# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_remove_department_university'),
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('gravatar_url', models.URLField(blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('token_version', models.CharField(default=b'3353d8ef-5b58-4ce7-aa6a-1f276d335500', unique=True, max_length=36, db_index=True)),
                ('department', models.ForeignKey(to='departments.Department')),
                ('university', models.ForeignKey(to='universities.University')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
