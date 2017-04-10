# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 01:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coursemanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortAnswerQuiz',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default=2)),
                ('questionPrompt', models.CharField(max_length=300)),
                ('correctAnswer', models.CharField(max_length=50)),
                ('LessonID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShortAnswerQuizResponse',
            fields=[
                ('responseID', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('quizID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.ShortAnswerQuiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
