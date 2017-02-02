from django.db import models

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length = 140)
	link = models.CharField(max_length = 10)
	youtube = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.title
	
	