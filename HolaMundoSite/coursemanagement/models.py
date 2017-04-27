from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User

from django.utils import timezone



# Courses can be assigned or be separate
class Lesson(models.Model):
	# Next
	# Prev
	lessonID = models.AutoField(primary_key=True)
	assignedCourse = models.ForeignKey('coursemanagement.Course', on_delete=models.CASCADE,
									   related_name='assigned_course', null=True, blank=True)
	title = models.CharField(max_length=55)
	youtube = models.CharField(max_length=100)
	author = models.ForeignKey(User, null=False, blank=False)

	# Increment or decrement when moving to the next or previous orders. Can give order to quizzes as well.
	order = models.PositiveSmallIntegerField(null=False, blank=False, default=1)

	NUM_TABS = (
		('ONE', '1'),
		('TWO', '2'),
		('THREE', '3'),
		('FOUR', '4'),
		('FIVE', '5'),
		('SIX', '6'),
	)

	link = models.CharField(max_length=15)
	tabs = models.CharField(max_length=5, choices=NUM_TABS, default="1")

	# Names for the Tabs
	tab1 = models.CharField(max_length=15, default="1")
	tab2 = models.CharField(max_length=15, default="2")
	tab3 = models.CharField(max_length=15, default="3")
	tab4 = models.CharField(max_length=15, default="4")
	tab5 = models.CharField(max_length=15, default="5")
	tab6 = models.CharField(max_length=15, default="6")

	# Hide the tabs that will not be used in the template/views
	tab1desc = models.TextField(max_length=2000, default="Tab 1 Description")
	tab2desc = models.TextField(max_length=2000, default="Tab 2 Description")
	tab3desc = models.TextField(max_length=2000, default="Tab 3 Description")
	tab4desc = models.TextField(max_length=2000, default="Tab 4 Description")
	tab5desc = models.TextField(max_length=2000, default="Tab 5 Description")
	tab6desc = models.TextField(max_length=2000, default="Tab 6 Description")

	tags = models.TextField(max_length=5000, default="")

	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)

	difficulty = models.CharField(max_length=15, choices=DIFFICULTIES, default="Beginner")
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	def __str__(self):
		return self.title


class Quiz(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key=True)
	LessonID = models.ForeignKey(Lesson, null=False, blank=False)
	title = models.CharField(max_length=55)

	# Potentially add the content of non-draggable sentence
	# content = models.CharField(max_length = 1000)

	# Words to Drag

	wordOne = models.CharField(max_length=15)
	wordTwo = models.CharField(max_length=15)
	wordThree = models.CharField(max_length=15)
	wordFour = models.CharField(max_length=15)
	wordFive = models.CharField(max_length=15)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	def __str__(self):
		return self.title


class Course(models.Model):
	courseID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=55)
	author = models.ForeignKey(User, null=False, blank=False)
	date = models.DateField(auto_now_add=True)
	link = models.CharField(max_length=15)
	
	# Text Field can work for the descripton, however, max length is not inforced at all which is not good.
	# Currently commented out for migrations/migrate
	description = models.CharField(max_length = 300, null = False, blank = False)

	
	difficulty = models.IntegerField()

	# quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	def __str__(self):
		return self.title

	# class Series(models.Model):
	# series_id = models.AutoField(primary_key = True)

# pass


class CourseLessonQuiz(models.Model):
	courseID = models.ForeignKey(Course, null=False, blank=False)
	LessonID = models.ForeignKey(Lesson, null=True, blank=True)
	QuizID = models.ForeignKey(Quiz, null=True, blank=True)
	position = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	class Meta:
		ordering = ['position']

	def __str__(self):
		return self.courseID.title


class MultipleChoiceQuiz(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key=True)
	LessonID = models.ForeignKey(Lesson, null=True, blank=True)
	title = models.CharField(max_length=55)
	author = models.ForeignKey(User, null=False, blank=False)

	NUMBER_OF_CHOICES = (
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
	)

	numberOfChoices = models.CharField(max_length=1, choices=NUMBER_OF_CHOICES, default="4")

	choiceOne = models.CharField(max_length=15, null=False, blank=False)
	choiceTwo = models.CharField(max_length=15, null=False, blank=False)
	choiceThree = models.CharField(max_length=15, null=True, blank=True)
	choiceFour = models.CharField(max_length=15, null=True, blank=True)
	choiceFive = models.CharField(max_length=15, null=True, blank=True)
	choiceSix = models.CharField(max_length=15, null=True, blank=True)

	CHOICES = (
		('A', '1'),
		('B', '2'),
		('C', '3'),
		('D', '4'),
		('E', '5'),
		('F', '6'),
	)

	correctAnswer = models.CharField(max_length=1, choices=CHOICES, default="A")

	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)

	difficulty = models.CharField(max_length=15, choices=DIFFICULTIES, default="Beginner")
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	def __str__(self):
		return self.title
		
class ShortAnswerQuiz(models.Model):
	quizID = models.AutoField(primary_key = True)
	LessonID = models.ForeignKey(Lesson, null = True, blank = False)
	title = models.CharField(max_length=55, null=False, blank=False)
	author = models.ForeignKey(User, null = False, blank = False)
	
	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)
	
	difficulty = models.IntegerField(choices=DIFFICULTIES, default=2)
	
	questionPrompt = models.CharField(max_length = 300, null=False, blank=False)
	correctAnswer = models.CharField(max_length =  50, null=False, blank=False)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)
	
	def __str__(self):
		return self.title

# Drag and Drop Quiz
# 15 Words
#	Either Choice Field or Integer

class DragAndDropQuiz(models.Model):
	quizID = models.AutoField(primary_key = True)
	LessonID = models.ForeignKey(Lesson, null = True, blank = False)
	title = models.CharField(max_length=55, null=False, blank=False)
	author = models.ForeignKey(User, null = False, blank = False)
	
	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)
	difficulty = models.IntegerField(choices=DIFFICULTIES, default=2)
	# WordCount may not be needed
	wordCount = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(15)])
	
	wordOne = models.CharField(max_length = 15, null = False, blank = False)
	wordTwo = models.CharField(max_length = 15, null = False, blank = False)
	wordThree = models.CharField(max_length = 15, null = False, blank = False)
	wordFour = models.CharField(max_length = 15, null = True, blank = True)
	wordFive = models.CharField(max_length = 15, null = True, blank = True)
	wordSix = models.CharField(max_length = 15, null = True, blank = True)
	wordSeven = models.CharField(max_length = 15, null = True, blank = True)
	wordEight = models.CharField(max_length = 15, null = True, blank = True)
	wordNine = models.CharField(max_length = 15, null = True, blank = True)
	wordTen = models.CharField(max_length = 15, null = True, blank = True)
	wordEleven = models.CharField(max_length = 15, null = True, blank = True)
	wordTwelve = models.CharField(max_length = 15, null = True, blank = True)
	wordThirteen = models.CharField(max_length = 15, null = True, blank = True)
	wordFourteen = models.CharField(max_length = 15, null = True, blank = True)
	wordFifteen = models.CharField(max_length = 15, null = True, blank = True)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)
	
class ShortAnswerQuizResponse(models.Model):
	responseID = models.AutoField(primary_key = True)
	quizID = models.ForeignKey(ShortAnswerQuiz, null = False, blank = False)
	user = models.ForeignKey(User, null = False, blank = False)
	score = models.IntegerField()
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)
	
	def __str__(self):
		return self.quizID.title + ": " + self.user.username


class MultipleChoiceQuizResponse(models.Model):
	responseID = models.AutoField(primary_key=True)
	quizID = models.ForeignKey(MultipleChoiceQuiz, null=False, blank=False)
	user = models.ForeignKey(User, null=False, blank=False)
	score = models.BooleanField(null=False, default=False)
	
	created_at = models.DateTimeField(auto_now_add=True, null = True)
	updated_at = models.DateTimeField(auto_now=True, null = True)

	def __str__(self):
		return self.quizID.title + ": " + self.user.username
