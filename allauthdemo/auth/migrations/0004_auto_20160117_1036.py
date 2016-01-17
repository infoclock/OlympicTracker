# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0003_auto_20160117_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demouser',
            name='school_year',
            field=models.IntegerField(verbose_name='school year', blank=True, null=True),
        ),
    ]
