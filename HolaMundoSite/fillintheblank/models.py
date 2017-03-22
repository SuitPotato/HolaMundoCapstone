from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
	question = models.CharField(max_length=250, default = '')
	answer = models.CharField(max_length=500, default = '')
	key = models.IntegerField(default=0)

	class Meta:
		db_table = "FillInTheBlank"

'''from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=500)

	def __str__(self):
		return self.choice_text
'''