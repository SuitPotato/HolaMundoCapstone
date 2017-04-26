from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


	
#This model holds the quiz id as the primary key, the author
#of the quiz gotten from the user table which is currently ocmmented
#out, the title of the quiz, an options field that can allow users to
#specify the amount questions/choices they want (might be deleted)
#and currently 8 char fields that hold the 4 questions and the 4
#correct choices for those questions. Commented out above those 8
#is code for possibly saving all questions/choices in 2 variables
#called left and right and each individual entry could be separated
#by a semi colon or something similar	
class Matching(models.Model):
	quizID = models.AutoField(primary_key = True)
	author = models.ForeignKey(User, null=False, blank=False, default = 1)
	title = models.CharField(max_length = 140)
	
	NUMBER_OPTIONS = (
	('2', '2'),
	('3','3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
	('12', '12'),
	('13', '13'),
	('14', '14'),
	('15', '15'),
	)
	
	CHOICE_OPTIONS = (
	('2', '2'),
	('3','3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
	('12', '12'),
	('13', '13'),
	('14', '14'),
	('15', '15'),
	)
	
	DIFFICULTY_OPTIONS = (
	('1', 'Beginner'),
	('2', 'Intermediate'),
	('3', 'Advanced'),
	)
	
	question_options = models.CharField(max_length=2, choices=NUMBER_OPTIONS, default='2')
	answer_options = models.CharField(max_length=2, choices=CHOICE_OPTIONS, default='2')
	
	difficulty = models.CharField(max_length=12, choices=DIFFICULTY_OPTIONS, default='1')
	
	left_one = models.CharField(max_length = 140)
	left_two = models.CharField(max_length = 140)
	left_three = models.CharField(max_length = 140, blank = True)
	left_four = models.CharField(max_length = 140, blank = True)
	left_five = models.CharField(max_length = 140, blank = True)
	left_six = models.CharField(max_length = 140, blank = True)
	left_seven = models.CharField(max_length = 140, blank = True)
	left_eight = models.CharField(max_length = 140, blank = True)
	left_nine = models.CharField(max_length = 140, blank = True)
	left_ten = models.CharField(max_length = 140, blank = True)
	left_eleven = models.CharField(max_length = 140, blank = True)
	left_twelve = models.CharField(max_length = 140, blank = True)
	left_thirteen = models.CharField(max_length = 140, blank = True)
	left_fourteen = models.CharField(max_length = 140, blank = True)
	left_fifteen = models.CharField(max_length = 140, blank = True)
	
	right_one = models.CharField(max_length = 140)
	right_two = models.CharField(max_length = 140)
	right_three = models.CharField(max_length = 140, blank = True)
	right_four = models.CharField(max_length = 140, blank = True)
	right_five = models.CharField(max_length = 140, blank = True)
	right_six = models.CharField(max_length = 140, blank = True)
	right_seven = models.CharField(max_length = 140, blank = True)
	right_eight = models.CharField(max_length = 140, blank = True)
	right_nine = models.CharField(max_length = 140, blank = True)
	right_ten = models.CharField(max_length = 140, blank = True)
	right_eleven = models.CharField(max_length = 140, blank = True)
	right_twelve = models.CharField(max_length = 140, blank = True)
	right_thirteen = models.CharField(max_length = 140, blank = True)
	right_fourteen = models.CharField(max_length = 140, blank = True)
	right_fifteen = models.CharField(max_length = 140, blank = True)
	
	'''rep1 = models.IntegerField(default = 0)
	rep2 = models.IntegerField(default = 0)
	rep3 = models.IntegerField(default = 0)
	rep4 = models.IntegerField(default = 0)
	rep5 = models.IntegerField(default = 0)
	rep6 = models.IntegerField(default = 0)
	rep7 = models.IntegerField(default = 0)
	rep8 = models.IntegerField(default = 0)
	rep9 = models.IntegerField(default = 0)
	rep10 = models.IntegerField(default = 0)
	rep11 = models.IntegerField(default = 0)
	rep12 = models.IntegerField(default = 0)
	rep13 = models.IntegerField(default = 0)
	rep14 = models.IntegerField(default = 0)
	rep15 = models.IntegerField(default = 0)
	
	answer0 = models.CharField(max_length = 140, blank = True)
	answer1 = models.CharField(max_length = 140, blank = True)
	answer2 = models.CharField(max_length = 140, blank = True)
	answer3 = models.CharField(max_length = 140, blank = True)
	answer4 = models.CharField(max_length = 140, blank = True)
	answer5 = models.CharField(max_length = 140, blank = True)
	answer6 = models.CharField(max_length = 140, blank = True)
	answer7 = models.CharField(max_length = 140, blank = True)
	answer8 = models.CharField(max_length = 140, blank = True)
	answer9 = models.CharField(max_length = 140, blank = True)
	answer10 = models.CharField(max_length = 140, blank = True)
	answer11 = models.CharField(max_length = 140, blank = True)
	answer12 = models.CharField(max_length = 140, blank = True)
	answer13 = models.CharField(max_length = 140, blank = True)
	answer14 = models.CharField(max_length = 140, blank = True)'''
	
	string = models.IntegerField(default = 0)
	
	#returns the quiz ID in string format in the database as the
	#identifier
	def __str__(self):
		return str(self.quizID)
		
#The answer model has a primary key AnswerId that is an automatically
#generated integer every time a student answers a question. The
#student field is currently commented out but is a foreign key to the
#user database that will save who the user is in the table. Another
#commented out field is an attempt on linking the two tables (Matching
#and Answer). The next four fields holds the Users answers, but
#following those four fields is a field that might be created to hold
#all the users answers in one variable (array) separated by semi colons
#or something similar allowing for dynamic amounts of fields. The next
#four fields will hold the questions that the user answered coming
#directly from the Matching table. The score attribute keeps track in
#thedatabase whether or not the student got the correct answer and
#defaults at 0 which means incorrect while 1 means correct. The function
#returns the answer id in string format as a representation of the
#unique answer in the database.
		
class Answer(models.Model):

	'''right_one = models.CharField(max_length = 140, blank = True)
	right_two = models.CharField(max_length = 140, blank = True)
	right_three = models.CharField(max_length = 140, blank = True)
	right_four = models.CharField(max_length = 140, blank = True)
	right_five = models.CharField(max_length = 140, blank = True)
	right_six = models.CharField(max_length = 140, blank = True)
	right_seven = models.CharField(max_length = 140, blank = True)
	right_eight = models.CharField(max_length = 140, blank = True)
	right_nine = models.CharField(max_length = 140, blank = True)
	right_ten = models.CharField(max_length = 140, blank = True)
	right_eleven = models.CharField(max_length = 140, blank = True)
	right_twelve = models.CharField(max_length = 140, blank = True)
	right_thirteen = models.CharField(max_length = 140, blank = True)
	right_fourteen = models.CharField(max_length = 140, blank = True)
	right_fifteen = models.CharField(max_length = 140, blank = True)
	
	
	ANSWER_OPTIONS = (
	('', '------------------------'),
	(right_one, right_one),
	(right_two, right_two),
	(right_three, right_three),
	(right_four, right_four),
	(right_five, right_five),
	(right_six, right_six),
	(right_seven, right_seven),
	(right_eight, right_eight),
	(right_nine, right_nine),
	(right_ten, right_ten),
	(right_eleven, right_eleven),
	(right_twelve, right_twelve),
	(right_thirteen, right_thirteen),
	(right_fourteen, right_fourteen),
	(right_fifteen, right_fifteen),
	)'''
	
	resultsID = models.AutoField(primary_key = True)
	
	title = models.CharField(max_length = 140, default = '')
	
	quizID = models.IntegerField(default = 0)
	#quizID = models.ForeignKey(Matching, null=False, blank=False)
	
	#user = models.ForeignKey(User, null=False, blank=False, default=1)
		
	answer_one = models.CharField(max_length = 140, blank = True)
	answer_two = models.CharField(max_length = 140, blank = True)
	answer_three = models.CharField(max_length = 140, blank = True)
	answer_four = models.CharField(max_length = 140, blank = True)
	answer_five = models.CharField(max_length = 140, blank = True)
	answer_six = models.CharField(max_length = 140, blank = True)
	answer_seven = models.CharField(max_length = 140, blank = True)
	answer_eight = models.CharField(max_length = 140, blank = True)
	answer_nine = models.CharField(max_length = 140, blank = True)
	answer_ten = models.CharField(max_length = 140, blank = True)
	answer_eleven = models.CharField(max_length = 140, blank = True)
	answer_twelve = models.CharField(max_length = 140, blank = True)
	answer_thirteen = models.CharField(max_length = 140, blank = True)
	answer_fourteen = models.CharField(max_length = 140, blank = True)
	answer_fifteen = models.CharField(max_length = 140, blank = True)
	
	left_one = models.CharField(max_length = 140, default = '')
	left_two = models.CharField(max_length = 140, default = '')
	left_three = models.CharField(max_length = 140, blank = True)
	left_four = models.CharField(max_length = 140, blank = True)
	left_five = models.CharField(max_length = 140, blank = True)
	left_six = models.CharField(max_length = 140, blank = True)
	left_seven = models.CharField(max_length = 140, blank = True)
	left_eight = models.CharField(max_length = 140, blank = True)
	left_nine = models.CharField(max_length = 140, blank = True)
	left_ten = models.CharField(max_length = 140, blank = True)
	left_eleven = models.CharField(max_length = 140, blank = True)
	left_twelve = models.CharField(max_length = 140, blank = True)
	left_thirteen = models.CharField(max_length = 140, blank = True)
	left_fourteen = models.CharField(max_length = 140, blank = True)
	left_fifteen = models.CharField(max_length = 140, blank = True)
	
	score = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)
	
	
	def __str__(self):
		#return str(self.title + ": " + self.user.username)
		return str(self.quizID)