from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

#model created for quiz name and number of choices in the database
'''class Number(models.Model):
	quiz_name = models.CharField(max_length=50, default = '')
	number = models.IntegerField()
	def __str__(self):
		return self.quiz_name
	
	#defining the name of the database table... possibly?
	class Meta:
		db_table = "matching"
		
#model created in database for the choice, the answer, and the
#corresponding letter to the answer	
class Question(models.Model):
	MN = Number(models.Model)
	copynumber = MN.number
	temp = 0
	#while(temp != copynumber):
	question = models.CharField(max_length=250, default = '')
	correct = models.CharField(max_length=250, default = '')
	rand_letter = models.CharField(max_length=1, default = '')
		#temp += 1
	def __str__(self):
		return self.question
	
	#do i use same db table or create new one?

#model in database to store users answer		
class Answer(models.Model):
	answer = models.CharField(max_length=1, default = '')
	def __str__(self):
		return self.answer
		
	#do i use same db table or create new one?'''
	
NUMBER_OPTIONS = (
	('2', '2'),
	('3','3'),
	('4', '4'),
	)
	
class Matching(models.Model):
	quizID = models.AutoField(primary_key = True)
	#author = models.ForeignKey(User, null=False, blank=False)
	title = models.CharField(max_length = 140)
	
	NUMBER_OPTIONS = (
	('2', '2'),
	('3','3'),
	('4', '4'),
	)
	options = models.CharField(max_length=10, choices=NUMBER_OPTIONS, default='4')
	
	left_one = models.CharField(max_length = 20, blank = True)
	left_two = models.CharField(max_length = 20, blank = True)
	left_three = models.CharField(max_length = 20, blank = True)
	left_four = models.CharField(max_length = 20, blank = True)
	
	right_one = models.CharField(max_length = 20, blank = True)
	right_two = models.CharField(max_length = 20, blank = True)
	right_three = models.CharField(max_length = 20, blank = True)
	right_four = models.CharField(max_length = 20, blank = True)
	
	def __str__(self):
		return self.title
		
'''class Answer(models.Model):
	QuizID = models.ForeignKey(Matching, primary_key = True)
	title = models.ForeignKey(Matching)
	
	answer_one = models.CharField(max_length = 20, blank = True)
	answer_two = models.CharField(max_length = 20, blank = True)
	answer_three = models.CharField(max_length = 20, blank = True)
	answer_four = models.CharField(max_length = 20, blank = True)
	
	def __str__(self):
		return self.title'''