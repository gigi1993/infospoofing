# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visited', models.CharField(max_length=120, default='')),
                ('ip_address', models.CharField(max_length=120, default='')),
                ('asn', models.CharField(max_length=15, default='')),
                ('country', models.CharField(max_length=5, default='')),
            ],
        ),
    ]
