from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MatchingNumber(models.Model):
	number = models.IntegerField()
	def __str__(self):
		return self.number
	
class MatchingQuestion(models.Model):
	question = models.CharField(max_length=250)
	answer = models.CharField(max_length=250)
	rand_letter = models.CharField(max_length=1)
	def __str__(self):
		return self.question
		
class Answer(models.Model):
	answer = models.CharField(max_length=1)
	def __str__(self):
		return self.answer