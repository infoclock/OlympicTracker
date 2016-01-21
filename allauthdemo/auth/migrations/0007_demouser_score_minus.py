# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0006_demouser_score_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='demouser',
            name='score_minus',
            field=models.SmallIntegerField(default=0, verbose_name='scor extra'),
        ),
    ]
