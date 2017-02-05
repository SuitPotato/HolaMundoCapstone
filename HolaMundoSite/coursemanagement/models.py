from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Potentially hard code the next and previous keys
# ##############################################################
# Course Class Model 
# The course model is comprised of:
#	1. Videos
#	2. Quizzes
#
# Videos contain / require:
#	1. A title (charfield:140)
#	2. Youtube Link (charfield:100)
#	3. Tab (1-4) (charfield, max_length:15)
#		- Potentially add the ability to increase the number of tabs or decrease
#	4. Tab Description (textfield, max_length:2000)
#	5. Next Video / Quiz
#	6. Prev Video / Quiz
#	7. Video Order
#
# Quizzes contain / require:
#	??? Work on Later ???
#	1. Next
#	2. Prev
#	3. Video Order
# ##############################################################
# Lesson Class Model
#
#
# ##############################################################
# Many-to-One Relationship
# 1. Videos
# 2. Quizzes

# To reference a model from another app:
#	models.foreignkey(appname.modelname)
class Course(models.Model):
	course_title = models.CharField(max_length = 140)
	course_id = models.AutoField(primary_key = True)
	
	pass
	#def __str__(self):
	
	
class Videos(models.Model):
	#title = models.CharField(max_length = 140)
	#youtube = models.CharField(max_length = 100)
	# Tab (1-4)
	# Tab Description (1-4)
	# Next
	# Prev
	pass
	
class Series(models.Model):
	#series_id = models.AutoField(primary_key = True)
	pass
	