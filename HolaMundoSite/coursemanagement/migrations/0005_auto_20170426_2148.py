# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-27 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0004_auto_20170426_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draganddropquiz',
            name='title',
            field=models.CharField(max_length=55),
        ),
    ]
