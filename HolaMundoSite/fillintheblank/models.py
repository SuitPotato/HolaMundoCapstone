from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Fill In The Blank Question Model
class FillInTheBlankQuestion(models.Model):
	# questionID references primary key
	questionID = models.AutoField(primary_key = True)
	# title of the question
	title = models.CharField(max_length = 100)
	# author of question
	author = models.CharField(max_length = 100)
	# Beginning of sentence
	question_start = models.CharField(max_length = 50)
	# End of sentence
	question_end = models.CharField(max_length = 50)
	# Answer for Fill In The Blank
	answer = models.CharField(max_length = 100)
	# Correct Answer for Fill in the Blank
	correctAnswer = models.CharField(max_length=100, default='')


	def __str__(self):
		return self.title
