# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0008_auto_20160508_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demouser',
            name='infoarena_handle',
        ),
        migrations.RemoveField(
            model_name='demouser',
            name='school_year',
        ),
        migrations.RemoveField(
            model_name='demouser',
            name='score_csacademy',
        ),
        migrations.RemoveField(
            model_name='demouser',
            name='score_extra',
        ),
        migrations.RemoveField(
            model_name='demouser',
            name='score_fmi_no_stress',
        ),
        migrations.RemoveField(
            model_name='demouser',
            name='score_minus',
        ),
    ]
