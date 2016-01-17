# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import allauthdemo.auth.models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('first_name', models.CharField(null=True, blank=True, max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(null=True, blank=True, max_length=40, verbose_name='last name')),
                ('display_name', models.CharField(null=True, blank=True, max_length=14, verbose_name='display name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'db_table': 'auth_user',
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', allauthdemo.auth.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user', primary_key=True)),
                ('avatar_url', models.CharField(null=True, blank=True, max_length=256)),
                ('dob', models.DateField(null=True, blank=True, verbose_name='dob')),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='demouser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_set', to='auth.Group', related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='demouser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_set', to='auth.Permission', related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.'),
        ),
    ]
