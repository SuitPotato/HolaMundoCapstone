# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fillintheblank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillintheblankquestion',
            name='correctAnswer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fillintheblankquestion',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]