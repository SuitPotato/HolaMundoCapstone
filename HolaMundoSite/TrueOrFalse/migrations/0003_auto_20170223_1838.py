# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrueOrFalse', '0002_auto_20170223_1810'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_text',
            field=models.CharField(default='Fill in', max_length=5),
            preserve_default=False,
        ),
    ]