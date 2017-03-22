from __future__ import unicode_literals
from django.db import models


# Required for importing User for Author 
from django.contrib.auth.models import User


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
#class Course(models.Model):
	#course_title = models.CharField(max_length = 140)
	#course_id = models.AutoField(primary_key = True)
	
#	pass
	#def __str__(self):


# Courses can be assigned or be separate
class Lesson(models.Model):
	# Next
	# Prev
	lessonID = models.AutoField(primary_key = True)
	assignedCourse = models.ForeignKey('coursemanagement.Course', on_delete=models.CASCADE,related_name='assigned_course',null = True, blank = True)
	title = models.CharField(max_length = 140)
	youtube = models.CharField(max_length = 100)
	author = models.ForeignKey(User, null=False, blank=False)
	
	# Increment or decrement when moving to the next or previous orders. Can give order to quizzes as well.
	order = models.PositiveSmallIntegerField(null=False, blank=False, default = 1)
	
	NUM_TABS = (
	('ONE', '1'),
	('TWO', '2'),
	('THREE','3'),
	('FOUR', '4'),
	('FIVE','5'),
	('SIX','6'),
	)
	
	link = models.CharField(max_length = 15)
	tabs = models.CharField(max_length = 5, choices = NUM_TABS, default="1")
	
	# Names for the Tabs
	tab1 = models.CharField(max_length=15, default = "1")
	tab2 = models.CharField(max_length=15, default = "2")
	tab3 = models.CharField(max_length=15, default = "3")
	tab4 = models.CharField(max_length=15, default = "4")
	tab5 = models.CharField(max_length=15, default = "5")
	tab6 = models.CharField(max_length=15, default = "6")
	
	# Hide the tabs that will not be used in the template/views
	tab1desc = models.TextField(max_length = 2000, default = "Tab 1 Description")
	tab2desc = models.TextField(max_length = 2000, default = "Tab 2 Description")
	tab3desc = models.TextField(max_length = 2000, default = "Tab 3 Description")
	tab4desc = models.TextField(max_length = 2000, default = "Tab 4 Description")
	tab5desc = models.TextField(max_length = 2000, default = "Tab 5 Description")
	tab6desc = models.TextField(max_length = 2000, default = "Tab 6 Description")
	
	def __str__(self):
		return self.title
		
class Course(models.Model):
	courseID = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100)
	author = models.ForeignKey(User, null=False, blank=False)
	date = models.DateField(auto_now_add = True)
	lesson = models.ManyToManyField(Lesson, null=False, blank=False)
	#quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	
	
	
	def __str__(self):
		return self.title
		
#class Series(models.Model):
	#series_id = models.AutoField(primary_key = True)
#	pass
	
