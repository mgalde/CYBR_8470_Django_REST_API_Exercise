# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_breed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='eventtype',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='userid',
        ),
    ]
