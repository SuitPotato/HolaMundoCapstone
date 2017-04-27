from __future__ import unicode_literals

from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

# Create your models here.

class DragAndDrop(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 55)
	
	# Text Content
	content = models.CharField(max_length = 1000)
	
	# Text to Drag
	wordOne = models.CharField(max_length = 15)
	wordTwo = models.CharField(max_length = 15)
	wordThree = models.CharField(max_length = 15)
	wordFour = models.CharField(max_length = 15)
	wordFive = models.CharField(max_length = 15)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)
	
	
	def __str__(self):
		return self.title
		
