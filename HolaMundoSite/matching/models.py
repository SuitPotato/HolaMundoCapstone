from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MatchingNumber(models.Model):
	number = forms.IntegerField(label='How many matching questions do you want?', max_length=20)
	def __str__(self):
		return self.number
	
class MatchingQuestion(models.Model):
	question = forms.CharField(label='Question:', max_length=100)
	def __str__(self):
		return self.question