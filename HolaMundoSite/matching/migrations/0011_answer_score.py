# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0010_remove_answer_quizid'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
