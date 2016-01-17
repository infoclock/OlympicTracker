# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
