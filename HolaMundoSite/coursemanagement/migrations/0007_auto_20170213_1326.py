# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0006_lesson_assignedcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lesson',
            field=models.ManyToManyField(blank=True, null=True, to='coursemanagement.Lesson'),
        ),
    ]