# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='codeforces_handle',
            field=models.CharField(blank=True, null=True, verbose_name='codeforces handle', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='infoarena_handle',
            field=models.CharField(blank=True, null=True, verbose_name='infoarena handle', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='school'),
        ),
    ]
