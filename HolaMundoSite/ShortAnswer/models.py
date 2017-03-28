from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Short Answer/Essay Question Model
class Question(models.Model):
	# primary key references quiestionID
	questionID = models.AutoField(primary_key = True)
	# title of question
	title = models.CharField(max_length = 1000)
	# author of quiz
	author = models.CharField(max_length = 100)
	# Text Field for Question
	question = models.CharField(max_length = 1000)
	# Text Field for answer
	answer = models.CharField(max_length = 1000)
	# Text field for Correct Answer
	correctAnswer = models.CharField(max_length=1000, default='')
	# score to track performance of User
	score = models.CharField(max_length=100, default='')


	def __str__(self):
		return self.title

	
