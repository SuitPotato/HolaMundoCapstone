# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 05:16
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coursemanagement', '0003_auto_20170426_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='DragAndDropQuiz',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default=2)),
                ('wordCount', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default=6, max_length=2)),
                ('word1', models.CharField(max_length=15)),
                ('word2', models.CharField(max_length=15)),
                ('word3', models.CharField(max_length=15)),
                ('word4', models.CharField(blank=True, max_length=15, null=True)),
                ('word5', models.CharField(blank=True, max_length=15, null=True)),
                ('word6', models.CharField(blank=True, max_length=15, null=True)),
                ('word7', models.CharField(blank=True, max_length=15, null=True)),
                ('word8', models.CharField(blank=True, max_length=15, null=True)),
                ('word9', models.CharField(blank=True, max_length=15, null=True)),
                ('word10', models.CharField(blank=True, max_length=15, null=True)),
                ('word11', models.CharField(blank=True, max_length=15, null=True)),
                ('word12', models.CharField(blank=True, max_length=15, null=True)),
                ('word13', models.CharField(blank=True, max_length=15, null=True)),
                ('word14', models.CharField(blank=True, max_length=15, null=True)),
                ('word15', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchingQuiz',
            fields=[
                ('quizID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('difficulty', models.IntegerField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default=2)),
                ('numberOfOptions', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default=6, max_length=2)),
                ('promptOne', models.CharField(max_length=25)),
                ('answerOne', models.CharField(max_length=25)),
                ('promptTwo', models.CharField(max_length=25)),
                ('answerTwo', models.CharField(max_length=25)),
                ('promptThree', models.CharField(blank=True, max_length=25, null=True)),
                ('answerThree', models.CharField(blank=True, max_length=25, null=True)),
                ('promptFour', models.CharField(blank=True, max_length=25, null=True)),
                ('answerFour', models.CharField(blank=True, max_length=25, null=True)),
                ('promptFive', models.CharField(blank=True, max_length=25, null=True)),
                ('answerFive', models.CharField(blank=True, max_length=25, null=True)),
                ('promptSix', models.CharField(blank=True, max_length=25, null=True)),
                ('answerSix', models.CharField(blank=True, max_length=25, null=True)),
                ('promptSeven', models.CharField(blank=True, max_length=25, null=True)),
                ('answerSeven', models.CharField(blank=True, max_length=25, null=True)),
                ('promptEight', models.CharField(blank=True, max_length=25, null=True)),
                ('answerEight', models.CharField(blank=True, max_length=25, null=True)),
                ('promptNine', models.CharField(blank=True, max_length=25, null=True)),
                ('answerNine', models.CharField(blank=True, max_length=25, null=True)),
                ('promptTen', models.CharField(blank=True, max_length=25, null=True)),
                ('answerTen', models.CharField(blank=True, max_length=25, null=True)),
                ('promptEleven', models.CharField(blank=True, max_length=25, null=True)),
                ('answerEleven', models.CharField(blank=True, max_length=25, null=True)),
                ('promptTwelve', models.CharField(blank=True, max_length=25, null=True)),
                ('answerTwelve', models.CharField(blank=True, max_length=25, null=True)),
                ('promptThirteen', models.CharField(blank=True, max_length=25, null=True)),
                ('answerThirteen', models.CharField(blank=True, max_length=25, null=True)),
                ('promptFourteen', models.CharField(blank=True, max_length=25, null=True)),
                ('answerFourteen', models.CharField(blank=True, max_length=25, null=True)),
                ('promptFifteen', models.CharField(blank=True, max_length=25, null=True)),
                ('answerFifteen5', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab1desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab2desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab3desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab4desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab5desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tab6desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='multiplechoicequiz',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='shortanswerquiz',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='matchingquiz',
            name='LessonID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson'),
        ),
        migrations.AddField(
            model_name='matchingquiz',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='draganddropquiz',
            name='LessonID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson'),
        ),
        migrations.AddField(
            model_name='draganddropquiz',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
