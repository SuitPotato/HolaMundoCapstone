from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Create your models here.

# Model for Fill In The Blank Question
class Question(models.Model):
	# questionID references primary key
	questionID = models.AutoField(primary_key = True)
	# title of question
	title = models.CharField(max_length = 50)
	# author of question is User logged in
	author = models.ForeignKey(User, null=False, blank=False, default = 1, related_name='fb_author')
	# start of question
	question_start = models.CharField(max_length = 100, null=True, blank=True)
	# end of question
	question_end = models.CharField(max_length = 100, null=True, blank=True)
	# correctAnswer for question 
	correctAnswer = models.CharField(max_length = 100, default = '')

	# Difficulty for Content Creator to Create
	DIFFICULTIES = (
		('1', 'Beginner'),
		('2', 'Intermediate'),
		('3', 'Advanced'),
		)
	difficulty = models.CharField(max_length = 15, choices=DIFFICULTIES, default="Beginner")

	def __str__(self):
		return self.title

# Model for Fill In The Blank Answer
class Answer(models.Model):
	# answerID references primary key
	answerID = models.AutoField(primary_key = True)
	# title for quiz to answer
	question = models.ForeignKey(Question, null=False, blank=False)
	# Student's answerID
	answer = models.CharField(max_length = 100)
	# score to track Student's performance
	score = models.IntegerField(default = 0)
	# total for score
	total = models.IntegerField(default = 0)
	# user taking quiz
	user = models.ForeignKey(User, null = False, blank = False, default = 1)

	def __str__(self):
		return str(self.answerID)
