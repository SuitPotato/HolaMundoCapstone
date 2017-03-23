from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Short Answer/Essay Question Model
class Question(models.Model):
	# Text Field for Question
	question = models.CharField(max_length=250, default = '')
	# Text Field for answer
	answer = models.CharField(max_length=500, default = '')
	# Key for question
	key = models.IntegerField(default=0)

	class Meta:
		db_table = "FillInTheBlank"

class Answer(models.Model):
	answer = models.CharField(max_length=500, default = '')

	def __str__(self):
		return self.answer

# Fill In The Blank Question Model
class FillInTheBlankQuestion(models.Model):
	# Beginning of sentence
	question_start = models.CharField(max_length=50, default = '')
	# End of sentence
	question_end = models.CharField(max_length=50, default = '')
	# Answer for Fill In The Blank
	answer = models.CharField(max_length=50, default = '')
	# Key for question
	key = models.IntegerField(default=0)

	def __str__(self):
		return self.answer
