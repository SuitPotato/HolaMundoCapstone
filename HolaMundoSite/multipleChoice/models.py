from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Response(models.Model):
    responseID = models.AutoField(primary_key = True)
    #title = models.CharField(max_length=1500, default = '')

    answer = models.CharField(max_length=150, default='')
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.responseID)

    # class Meta:
    #      db_table = "multipleChoice"


class Quiz(models.Model):

    quizID = models.AutoField(primary_key = True)
    title = models.CharField(max_length=1500, default = '')
    answerA = models.CharField(max_length=150, default='')
    answerB = models.CharField(max_length=150, default='')
    answerC = models.CharField(max_length=150, default='')
    answerD = models.CharField(max_length=150, default='')
    score = models.CharField(max_length=150, default='')
    correctAnswer = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = "multipleChoice"
