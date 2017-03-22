# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 22:00
# Generated by Django 1.10.5 on 2017-03-22 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DragAndDrop',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('content', models.CharField(max_length=1000)),
                ('wordOne', models.CharField(max_length=15)),
                ('wordTwo', models.CharField(max_length=15)),
                ('wordThree', models.CharField(max_length=15)),
                ('wordFour', models.CharField(max_length=15)),
                ('wordFive', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('wordOne', models.CharField(max_length=15)),
                ('wordTwo', models.CharField(max_length=15)),
                ('wordThree', models.CharField(max_length=15)),
                ('wordFour', models.CharField(max_length=15)),
                ('wordFive', models.CharField(max_length=15)),
            ],
        ),
    ]
