# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0002_auto_20160117_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='codeforces_handle',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='infoarena_handle',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='school_year',
        ),
        migrations.AddField(
            model_name='demouser',
            name='codeforces_handle',
            field=models.CharField(blank=True, verbose_name='codeforces handle', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='demouser',
            name='infoarena_handle',
            field=models.CharField(blank=True, verbose_name='infoarena handle', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='demouser',
            name='school_year',
            field=models.IntegerField(blank=True, verbose_name='school', null=True),
        ),
    ]
