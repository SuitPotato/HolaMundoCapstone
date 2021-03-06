from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Required for importing User for Author
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Courses can be assigned or be separate
class Lesson(models.Model):
	# Next
	# Prev
	lessonID = models.AutoField(primary_key=True)
	assignedCourse = models.ForeignKey('coursemanagement.Course', on_delete=models.CASCADE,
									   related_name='assigned_course', null=True, blank=True)
	title = models.CharField(max_length=140)
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


	tab1desc = RichTextField()
	tab2desc = RichTextField()
	tab3desc = RichTextField()
	tab4desc = RichTextField()
	tab5desc = RichTextField()
	tab6desc = RichTextField()

	tags = models.TextField(max_length=5000, default="")

	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)

	difficulty = models.CharField(max_length=15, choices=DIFFICULTIES, default="Beginner")

	def __str__(self):
		return self.title


class Course(models.Model):
	courseID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=30)
	author = models.ForeignKey(User, null=False, blank=False)
	date = models.DateField(auto_now_add=True)


	# Text Field can work for the descripton, however, max length is not inforced at all which is not good.
	# Currently commented out for migrations/migrate
	description = models.CharField(max_length = 300, null = False, blank = False)


	difficulty = models.IntegerField()



	def __str__(self):
		return self.title


class Quiz(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key=True)
	assignedCourse = models.ForeignKey(Course, null=False, blank=False)
	title = models.CharField(max_length=140)

	# Potentially add the content of non-draggable sentence
	# content = models.CharField(max_length = 1000)

	# Words to Drag

	wordOne = models.CharField(max_length=15)
	wordTwo = models.CharField(max_length=15)
	wordThree = models.CharField(max_length=15)
	wordFour = models.CharField(max_length=15)
	wordFive = models.CharField(max_length=15)

	def __str__(self):
		return self.title



class CourseLessonQuiz(models.Model):
	relationID = models.AutoField(primary_key=True)
	courseID = models.ForeignKey(Course, null=False, blank=False)
	LessonID = models.ForeignKey(Lesson, null=True, blank=True)
	QuizID = models.ForeignKey(Quiz, null=True, blank=True)
	position = models.PositiveIntegerField(validators=[MaxValueValidator(30)], null=True, blank=True)

	class Meta:
		ordering = ['position']

	def __str__(self):
		return self.courseID.title


class MultipleChoiceQuiz(models.Model):
	# QuizID - References the Primary Key
	quizID = models.AutoField(primary_key=True)
	assignedCourse = models.ForeignKey(Course, null=True, blank=True)
	title = models.CharField(max_length=140)
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

	def __str__(self):
		return self.title

class ShortAnswerQuiz(models.Model):
	quizID = models.AutoField(primary_key = True)
	LessonID = models.ForeignKey(Lesson, null = True, blank = False)
	title = models.CharField(max_length=100, null=False, blank=False)
	author = models.ForeignKey(User, null = False, blank = False)

	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)

	difficulty = models.IntegerField(choices=DIFFICULTIES, default=2)

	questionPrompt = models.CharField(max_length = 300, null=False, blank=False)
	correctAnswer = models.CharField(max_length =  50, null=False, blank=False)

	def __str__(self):
		return self.title

# Drag and Drop Quiz
# 15 Words
#	Either Choice Field or Integer

class DragAndDropQuiz(models.Model):
	quizID = models.AutoField(primary_key = True)
	LessonID = models.ForeignKey(Lesson, null = True, blank = False)
	title = models.CharField(max_length=100, null=False, blank=False)
	author = models.ForeignKey(User, null = False, blank = False)
	
	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)

	difficulty = models.CharField(max_length=15, choices=DIFFICULTIES, default="Beginner")
	# WordCount may not be needed
	
	NUMBER_OF_WORDS = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),
		('11','11'),
		('12','12'),
		('13','13'),
		('14','14'),
		('15','15'),
	)
	
	wordCount = models.CharField(max_length=2, choices=NUMBER_OF_WORDS, default = 6)
	
	word1 = models.CharField(max_length = 15, null = False, blank = False)
	word2 = models.CharField(max_length = 15, null = False, blank = False)
	word3 = models.CharField(max_length = 15, null = False, blank = False)
	word4 = models.CharField(max_length = 15, null = True, blank = True)
	word5 = models.CharField(max_length = 15, null = True, blank = True)
	word6 = models.CharField(max_length = 15, null = True, blank = True)
	word7 = models.CharField(max_length = 15, null = True, blank = True)
	word8 = models.CharField(max_length = 15, null = True, blank = True)
	word9 = models.CharField(max_length = 15, null = True, blank = True)
	word10 = models.CharField(max_length = 15, null = True, blank = True)
	word11 = models.CharField(max_length = 15, null = True, blank = True)
	word12 = models.CharField(max_length = 15, null = True, blank = True)
	word13 = models.CharField(max_length = 15, null = True, blank = True)
	word14 = models.CharField(max_length = 15, null = True, blank = True)
	word15 = models.CharField(max_length = 15, null = True, blank = True)
	
class ShortAnswerQuizResponse(models.Model):
	responseID = models.AutoField(primary_key = True)
	quizID = models.ForeignKey(ShortAnswerQuiz, null = False, blank = False)
	user = models.ForeignKey(User, null = False, blank = False)
	score = models.IntegerField()

	def __str__(self):
		return self.quizID.title + ": " + self.user.username


class MultipleChoiceQuizResponse(models.Model):
	responseID = models.AutoField(primary_key=True)
	quizID = models.ForeignKey(MultipleChoiceQuiz, null=False, blank=False)
	user = models.ForeignKey(User, null=False, blank=False)
	score = models.BooleanField(null=False, default=False)

	def __str__(self):
		return self.quizID.title + ": " + self.user.username

class MatchingQuiz(models.Model):
	quizID = models.AutoField(primary_key = True)
	LessonID = models.ForeignKey(Lesson, null = True, blank = True)
	title = models.CharField(max_length = 140)
	author = models.ForeignKey(User, null = False, blank = False)
	
	NUMBER_OF_OPTIONS = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),
		('11','11'),
		('12','12'),
		('13','13'),
		('14','14'),
		('15','15'),
	)
	
	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
	)
	
	difficulty = models.IntegerField(choices=DIFFICULTIES, default=2)
	numberOfOptions = models.CharField(max_length=2, choices=NUMBER_OF_OPTIONS, default = 6)
	
	promptOne = models.CharField(max_length = 25, null = False, blank = False)
	answerOne = models.CharField(max_length = 25, null = False, blank = False)
	promptTwo = models.CharField(max_length = 25, null = False, blank = False)
	answerTwo = models.CharField(max_length = 25, null = False, blank = False)
	promptThree = models.CharField(max_length = 25, null = True, blank = True)
	answerThree = models.CharField(max_length = 25, null = True, blank = True)
	promptFour = models.CharField(max_length = 25, null = True, blank = True)
	answerFour = models.CharField(max_length = 25, null = True, blank = True)
	promptFive = models.CharField(max_length = 25, null = True, blank = True)
	answerFive = models.CharField(max_length = 25, null = True, blank = True)
	promptSix = models.CharField(max_length = 25, null = True, blank = True)
	answerSix = models.CharField(max_length = 25, null = True, blank = True)
	promptSeven = models.CharField(max_length = 25, null = True, blank = True)
	answerSeven = models.CharField(max_length = 25, null = True, blank = True)
	promptEight = models.CharField(max_length = 25, null = True, blank = True)
	answerEight = models.CharField(max_length = 25, null = True, blank = True)
	promptNine = models.CharField(max_length = 25, null = True, blank = True)
	answerNine = models.CharField(max_length = 25, null = True, blank = True)
	promptTen = models.CharField(max_length = 25, null = True, blank = True)
	answerTen = models.CharField(max_length = 25, null = True, blank = True)
	promptEleven = models.CharField(max_length = 25, null = True, blank = True)
	answerEleven = models.CharField(max_length = 25, null = True, blank = True)
	promptTwelve = models.CharField(max_length = 25, null = True, blank = True)
	answerTwelve = models.CharField(max_length = 25, null = True, blank = True)
	promptThirteen = models.CharField(max_length = 25, null = True, blank = True)
	answerThirteen = models.CharField(max_length = 25, null = True, blank = True)
	promptFourteen = models.CharField(max_length = 25, null = True, blank = True)
	answerFourteen = models.CharField(max_length = 25, null = True, blank = True)
	promptFifteen = models.CharField(max_length = 25, null = True, blank = True)
	answerFifteen5 = models.CharField(max_length = 25, null = True, blank = True)
	
	
	
	