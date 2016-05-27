# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0009_auto_20160508_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='demouser',
            name='problems_solved_first_exam',
            field=models.PositiveSmallIntegerField(verbose_name='problems solved first exam', default=0),
        ),
        migrations.AddField(
            model_name='demouser',
            name='problems_solved_second_exam',
            field=models.PositiveSmallIntegerField(verbose_name='problems solved second exam', default=0),
        ),
    ]
