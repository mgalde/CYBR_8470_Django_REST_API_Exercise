# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20181004_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='breedsize',
            field=models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Med', 'Med'), ('Large', 'Large')], max_length=1000),
        ),
    ]