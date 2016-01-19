# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0005_auto_20160117_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='demouser',
            name='score_extra',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='scor extra'),
        ),
    ]
