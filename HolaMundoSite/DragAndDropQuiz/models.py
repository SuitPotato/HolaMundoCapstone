from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Create your models here.

class DragAndDrop(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 140)
	
	# Text Contetn
	content = models.CharField(max_length = 1000)
	
	# Text to Drag
	wordOne = models.CharField(max_length = 15)
	wordTwo = models.CharField(max_length = 15)
	wordThree = models.CharField(max_length = 15)
	wordFour = models.CharField(max_length = 15)
	wordFive = models.CharField(max_length = 15)
	
	
	def __str__(self):
		return self.title