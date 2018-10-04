# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181004_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='breedsize',
            field=models.IntegerField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dogage',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dogbreed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Breed'),
        ),
    ]
