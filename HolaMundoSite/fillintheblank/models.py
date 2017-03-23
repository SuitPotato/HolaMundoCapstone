from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Short Answer/Essay Question Model
class Question(models.Model):
	# primary key references quiestionID
	questionID = models.AutoField(primary_key = True, default = 'DEFAULT VALUE')
	# title of question
	title = models.CharField(max_length = 100, default = '')
	# author of quiz
	author = models.ForeignKey(User, null=False, blank=False, default = '')
	# Text Field for Question
	question_name = models.CharField(max_length=500, default = '')
	# Text Field for answer
	answer = models.CharField(max_length=500, default = '')


	def __str__(self):
		return self.title

#class Answer(models.Model):
#	answer = models.CharField(max_length=500, default = '')
#
#	def __str__(self):
#		return self.answer

# Fill In The Blank Question Model
class FillInTheBlankQuestion(models.Model):
	# questionID references primary key
	questionID = models.AutoField(primary_key = True, default = 'DEFAULT VALUE')
	# title of the question
	title = models.CharField(max_length=100, default = '')
	# author of question
	author = models.ForeignKey(User, null=False, blank=False, default = '')
	# Beginning of sentence
	question_start = models.CharField(max_length=50, default = '')
	# End of sentence
	question_end = models.CharField(max_length=50, default = '')
	# Answer for Fill In The Blank
	answer = models.CharField(max_length=50, default = '')


	def __str__(self):
		return self.title
