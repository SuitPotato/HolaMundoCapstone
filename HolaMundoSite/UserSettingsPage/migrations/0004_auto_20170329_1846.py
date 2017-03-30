# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanagement', '0015_auto_20170328_2225'),
        ('UserSettingsPage', '0003_auto_20170328_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='fourthLastVid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth', to='coursemanagement.Lesson'),
        ),
        migrations.AddField(
            model_name='preference',
            name='secondLastVid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='coursemanagement.Lesson'),
        ),
        migrations.AddField(
            model_name='preference',
            name='thirdLastVid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third', to='coursemanagement.Lesson'),
        ),
    ]
