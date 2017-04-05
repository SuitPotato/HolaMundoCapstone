# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 19:18
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('link', models.CharField(max_length=15)),
                ('difficulty', models.CharField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default='Beginner', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseLessonQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(30)])),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lessonID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('youtube', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('link', models.CharField(max_length=15)),
                ('tabs', models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5'), ('SIX', '6')], default='1', max_length=5)),
                ('tab1', models.CharField(default='1', max_length=15)),
                ('tab2', models.CharField(default='2', max_length=15)),
                ('tab3', models.CharField(default='3', max_length=15)),
                ('tab4', models.CharField(default='4', max_length=15)),
                ('tab5', models.CharField(default='5', max_length=15)),
                ('tab6', models.CharField(default='6', max_length=15)),
                ('tab1desc', models.TextField(default='Tab 1 Description', max_length=2000)),
                ('tab2desc', models.TextField(default='Tab 2 Description', max_length=2000)),
                ('tab3desc', models.TextField(default='Tab 3 Description', max_length=2000)),
                ('tab4desc', models.TextField(default='Tab 4 Description', max_length=2000)),
                ('tab5desc', models.TextField(default='Tab 5 Description', max_length=2000)),
                ('tab6desc', models.TextField(default='Tab 6 Description', max_length=2000)),
                ('tags', models.TextField(default='', max_length=5000)),
                ('difficulty', models.CharField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default='Beginner', max_length=15)),
                ('assignedCourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_course', to='coursemanagement.Course')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('wordOne', models.CharField(max_length=15)),
                ('wordTwo', models.CharField(max_length=15)),
                ('wordThree', models.CharField(max_length=15)),
                ('wordFour', models.CharField(max_length=15)),
                ('wordFive', models.CharField(max_length=15)),
                ('LessonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='courselessonquiz',
            name='LessonID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson'),
        ),
        migrations.AddField(
            model_name='courselessonquiz',
            name='QuizID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Quiz'),
        ),
        migrations.AddField(
            model_name='courselessonquiz',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Course'),
        ),
    ]
