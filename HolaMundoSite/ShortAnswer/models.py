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

# Short Answer/Essay Answer Model
class Answer(models.Model):
	# foreign key should be linked to questionID of Question
	questionID = models.ForeignKey(Question, related_name='questioID_text')
	# foreign key should be linked to title of Question
	title = models.ForeignKey(Question, related_name='title_text')
	# foreign key should be linked to author of Question
	author = models.ForeignKey(Question, related_name='author_text')
	# foreign key should be linked to question of Question
	question = models.ForeignKey(Question, related_name='question_text')
	# text field for answer 
	answer = models.CharField(max_length=1000)
