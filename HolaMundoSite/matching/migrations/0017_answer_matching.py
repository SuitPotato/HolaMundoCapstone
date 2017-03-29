# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0016_remove_answer_matching'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='matching',
            field=models.ForeignKey(default='Help', on_delete=django.db.models.deletion.CASCADE, to='matching.Matching'),
        ),
    ]
