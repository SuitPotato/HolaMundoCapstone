# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0011_answer_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='match',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='matching.Matching'),
        ),
        migrations.AddField(
            model_name='matching',
            name='on',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='matching.Answer'),
        ),
    ]
