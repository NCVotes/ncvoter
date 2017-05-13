# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 15:19
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0011_changetracker_md5_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncvoter',
            name='birth_state',
            field=models.CharField(default='', max_length=2, verbose_name='birth state'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='changetracker',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]
