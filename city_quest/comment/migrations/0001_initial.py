# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 11:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30, verbose_name='Название квеста')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 12, 5, 11, 26, 36, 553518, tzinfo=utc), verbose_name='Дата начала квеста')),
                ('like', models.IntegerField(default=0, verbose_name='Количесвто лайков')),
                ('quest_id', models.IntegerField(default=0, verbose_name='Идентификатор квеста')),
            ],
        ),
    ]
