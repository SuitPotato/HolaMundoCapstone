from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User


# Create your models here.

# Model for Short Answer/Essay Question
class Question(models.Model):
	# questionID references primary key
	questionID = models.AutoField(primary_key = True)
	# title of the Question 
	title = models.CharField(max_length = 50)
	# author of Question is user logged in
	author = models.ForeignKey(User, null=False, blank=False, default = 1)
	# question 
	question = models.CharField(max_length = 100)
	# correctAnswer for question
	correctAnswer = models.CharField(max_length = 1000)

	# Difficulty of Question for Content Creator to create
	DIFFICULTIES = (
		('1', 'Beginner'),
		('2', 'Intermediate'),
		('3', 'Advanced'),
		)

	difficulty = models.CharField(max_length = 15, choices = DIFFICULTIES, default = "Beginner")

	def __str__(self):
		return self.title

# Model for Short Answer/Essay Answer 
class Answer(models.Model):
	# answerID references primary key 
	answerID = models.AutoField(primary_key = True)
	# title for quiz to answer
	title = models.CharField(max_length = 150, default = '')
	# Student's answer 
	answer = models.CharField(max_length = 1000)
	# score to track Student's performance
	score = models.IntegerField(default = 0)
	# total of score for User
	total = models.IntegerField(default = 0)
	# user taking quiz
	user = models.ForeignKey(User, null = False, blank = False, default = 1, related_name = 'shortAnswer_User')

	def __str__(self):
		return str(self.answerID)
	