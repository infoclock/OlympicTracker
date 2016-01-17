# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0004_auto_20160117_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='demouser',
            name='score_csacademy',
            field=models.PositiveSmallIntegerField(verbose_name='scor la csacademy', default=0),
        ),
        migrations.AddField(
            model_name='demouser',
            name='score_fmi_no_stress',
            field=models.PositiveSmallIntegerField(verbose_name='scor la fmi no stress', default=0),
        ),
        migrations.AlterField(
            model_name='demouser',
            name='school_year',
            field=models.PositiveSmallIntegerField(verbose_name='daca vrei sa echivalezi prima oara trece 1, daca vrei a doua oara trece 2', default=0),
        ),
    ]
