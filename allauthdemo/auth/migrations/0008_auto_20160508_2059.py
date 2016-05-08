# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0007_demouser_score_minus'),
    ]

    operations = [
        migrations.AddField(
            model_name='demouser',
            name='is_participating_2016',
            field=models.BooleanField(verbose_name='Partcipating 2015-2016 2nd semester', help_text='Partcipating 2015-2016 2nd semester', default=False),
        ),
        migrations.AlterField(
            model_name='demouser',
            name='score_minus',
            field=models.SmallIntegerField(verbose_name='scor minus', default=0),
        ),
    ]
