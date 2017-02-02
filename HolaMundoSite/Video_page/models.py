from django.db import models

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length = 140)
	link = models.CharField(max_length = 15)
	youtube = models.CharField(max_length = 100)
	tab1 = models.CharField(max_length = 15, default = "Tab 1")
	tab1desc = models.TextField(max_length = 2000, default = "Tab 1 Description")
	tab2 = models.CharField(max_length = 15, default = "Tab 2")
	tab2desc = models.TextField(max_length = 2000, default = "Tab 2 Description")
	tab3 = models.CharField(max_length = 15, default = "Tab 3")
	tab3desc = models.TextField(max_length = 2000, default = "Tab 3 Description")
	tab4 = models.CharField(max_length = 15, default = "Tab 4")
	tab4desc = models.TextField(max_length = 2000, default = "Tab 4 Description")
	
	def __str__(self):
		return self.title
	
	