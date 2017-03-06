from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=500)



 