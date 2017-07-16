# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0006_auto_20170603_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changetracker',
            name='ncid',
            field=models.CharField(db_index=True, max_length=12, verbose_name='ncid'),
        ),
        migrations.AlterField(
            model_name='ncvhis',
            name='county_id',
            field=models.SmallIntegerField(db_index=True, verbose_name='county_id'),
        ),
        migrations.AlterField(
            model_name='ncvhis',
            name='election_desc',
            field=models.CharField(blank=True, db_index=True, max_length=230, verbose_name='election_desc'),
        ),
        migrations.AlterField(
            model_name='ncvhis',
            name='ncid',
            field=models.CharField(db_index=True, max_length=12, verbose_name='ncid'),
        ),
        migrations.AlterField(
            model_name='ncvoter',
            name='county_id',
            field=models.SmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='ncvoter',
            name='ncid',
            field=models.CharField(db_index=True, max_length=12, unique=True, verbose_name='ncid'),
        ),
    ]
