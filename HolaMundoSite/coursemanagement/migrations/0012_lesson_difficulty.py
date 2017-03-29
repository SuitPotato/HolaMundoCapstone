# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0011_lesson_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3'), ('SIX', '6')], default='1', max_length=3),
        ),
    ]
