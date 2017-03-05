from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	answer_text = models.CharField(max_length=5)
	def __str__(self):
		return self.question_text
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=5)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
		
#class Answer(models.Model):
#	answer_text = models.CharField(max_length=5)
#	def __str__(self):
#		return self.answer_text