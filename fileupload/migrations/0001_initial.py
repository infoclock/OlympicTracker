# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import fileupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to=fileupload.models.user_directory_path)),
                ('slug', models.SlugField(blank=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('last_modified', models.DateField(auto_now=True, null=True)),
                ('problem', models.ForeignKey(null=True, to='demo.Problem')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
