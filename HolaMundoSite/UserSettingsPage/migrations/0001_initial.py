# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coursemanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('prefID', models.AutoField(primary_key=True, serialize=False)),
                ('defaultLanguage', models.CharField(choices=[('English', '1'), ('Spanish', '2')], default='1', max_length=10)),
                ('difficulty', models.CharField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Advanced', '3')], default='1', max_length=20)),
                ('fourthLastVid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth', to='coursemanagement.Lesson')),
                ('lastVid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanagement.Lesson')),
                ('secondLastVid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='coursemanagement.Lesson')),
                ('thirdLastVid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third', to='coursemanagement.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
