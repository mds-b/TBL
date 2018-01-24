# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 03:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20180124_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grat',
            name='groups',
            field=models.ManyToManyField(to='groups.Group', verbose_name='gRATs'),
        ),
        migrations.AlterField(
            model_name='irat',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='iRATs'),
        ),
    ]
