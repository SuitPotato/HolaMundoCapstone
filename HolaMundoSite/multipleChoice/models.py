from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    # id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150)
    answer_a = models.CharField(max_length=150, default='')
    answer_b = models.CharField(max_length=150, default='')
    answer_c = models.CharField(max_length=150, default='')
    answer_d = models.CharField(max_length=150, default='')

    #
    #
    class Meta:
        db_table = "multipleChoice"

# class Answer(models.Model):
#     answer_a = models.CharField(max_length=150)
#     answer_b = models.CharField(max_length=150)
#     answer_c = models.CharField(max_length=150)
#     answer_d = models.CharField(max_length=150)
#
#     class Meta:
#         db_table = "multipleChoice"
