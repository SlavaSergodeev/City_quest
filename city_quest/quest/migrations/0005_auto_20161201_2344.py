# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 13:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0004_auto_20161201_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 13, 44, 14, 786801, tzinfo=utc)),
        ),
    ]