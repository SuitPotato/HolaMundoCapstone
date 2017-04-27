from django import forms
from django.db import models
from django.forms import ModelForm
from matching.models import *
from django.contrib.auth.models import User
	
#the matching form calls the matching model and lists all of its fields
#in the fields array. Then the fields are again defined in the form
#as char fields. The quiz ID was being passed in as a hidden input but
#caused errors so it is currently commented out

'''class NumberForm(forms.Form):
	class Meta:
		model = Matching
		fields = ['question_options', 'answer_options',]
		
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
	
	question_options = forms.ChoiceField(choices = NUMBER_OPTIONS)
	answer_options = forms.ChoiceField(choices = NUMBER_OPTIONS)'''
	
class MatchingForm(forms.Form):
	class Meta:
		# Based off of the models
		model = Matching
		# Add options
		fields = ['title','difficulty', 'left_one',
		'left_two','left_three','left_four','left_five','left_six',
		'left_seven','left_eight','left_nine','left_ten',
		'left_eleven','left_twelve','left_thirteen','left_fourteen',
		'left_fifteen','right_one','right_two',
		'right_three','right_four','right_five','right_six',
		'right_seven', 'right_eight','right_nine','right_ten',
		'right_eleven','right_twelve','right_thirteen','right_fourteen',
		'right_fifteen',
		]
		
	# Fields defined under forms.
	
	title = forms.CharField(max_length = 140)
	
	DIFFICULTY_OPTIONS = (
	('1', 'Beginner'),
	('2', 'Intermediate'),
	('3', 'Advanced'),
	)
	
	difficulty = forms.ChoiceField(choices = DIFFICULTY_OPTIONS)
		
	left_one = forms.CharField(max_length = 140)
	left_two = forms.CharField(max_length = 140)
	left_three = forms.CharField(max_length = 140, required = False)
	left_four = forms.CharField(max_length = 140, required = False)
	left_five = forms.CharField(max_length = 140, required = False)
	left_six = forms.CharField(max_length = 140, required = False)
	left_seven = forms.CharField(max_length = 140, required = False)
	left_eight = forms.CharField(max_length = 140, required = False)
	left_nine = forms.CharField(max_length = 140, required = False)
	left_ten = forms.CharField(max_length = 140, required = False)
	left_eleven = forms.CharField(max_length = 140, required = False)
	left_twelve = forms.CharField(max_length = 140, required = False)
	left_thirteen = forms.CharField(max_length = 140, required = False)
	left_fourteen = forms.CharField(max_length = 140, required = False)
	left_fifteen = forms.CharField(max_length = 140, required = False)
	
	right_one = forms.CharField(max_length = 140)
	right_two = forms.CharField(max_length = 140)
	right_three = forms.CharField(max_length = 140, required = False)
	right_four = forms.CharField(max_length = 140, required = False)
	right_five = forms.CharField(max_length = 140, required = False)
	right_six = forms.CharField(max_length = 140, required = False)
	right_seven = forms.CharField(max_length = 140, required = False)
	right_eight = forms.CharField(max_length = 140, required = False)
	right_nine = forms.CharField(max_length = 140, required = False)
	right_ten = forms.CharField(max_length = 140, required = False)
	right_eleven = forms.CharField(max_length = 140, required = False)
	right_twelve = forms.CharField(max_length = 140, required = False)
	right_thirteen = forms.CharField(max_length = 140, required = False)
	right_fourteen = forms.CharField(max_length = 140, required = False)
	right_fifteen = forms.CharField(max_length = 140, required = False)
	
#The answer form calls the answer model in the database and sets the
#fields array to all of the fields inside of that table. Then those
#fields are redefined as char fields.
	
class AnswerForm(forms.Form):
	class Meta:
		model = Answer
		fields = ['answer_one', 'answer_two', 'answer_three',
				'answer_four','answer_five','answer_six','answer_seven',
				'answer_eight','answer_nine','answer_ten','answer_eleven',
				'answer_twelve','answer_thirteen','answer_fourteen',
				'answer_fifteen',]
	
	'''right_one = forms.CharField(max_length = 140, required = False)
	right_two = forms.CharField(max_length = 140, required = False)
	right_three = forms.CharField(max_length = 140, required = False)
	right_four = forms.CharField(max_length = 140, required = False)
	right_five = forms.CharField(max_length = 140, required = False)
	right_six = forms.CharField(max_length = 140, required = False)
	right_seven = forms.CharField(max_length = 140, required = False)
	right_eight = forms.CharField(max_length = 140, required = False)
	right_nine = forms.CharField(max_length = 140, required = False)
	right_ten = forms.CharField(max_length = 140, required = False)
	right_eleven = forms.CharField(max_length = 140, required = False)
	right_twelve = forms.CharField(max_length = 140, required = False)
	right_thirteen = forms.CharField(max_length = 140, required = False)
	right_fourteen = forms.CharField(max_length = 140, required = False)
	right_fifteen = forms.CharField(max_length = 140, required = False)
	
	ANSWER_OPTIONS = (
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

	answer_one = forms.CharField(max_length = 140, required = False)
	answer_two = forms.CharField(max_length = 140, required = False)
	answer_three = forms.CharField(max_length = 140, required = False)
	answer_four = forms.CharField(max_length = 140, required = False)
	answer_five = forms.CharField(max_length = 140, required = False)
	answer_six = forms.CharField(max_length = 140, required = False)
	answer_seven = forms.CharField(max_length = 140, required = False)
	answer_eight = forms.CharField(max_length = 140, required = False)
	answer_nine = forms.CharField(max_length = 140, required = False)
	answer_ten = forms.CharField(max_length = 140, required = False)
	answer_eleven = forms.CharField(max_length = 140, required = False)
	answer_twelve = forms.CharField(max_length = 140, required = False)
	answer_thirteen = forms.CharField(max_length = 140, required = False)
	answer_fourteen = forms.CharField(max_length = 140, required = False)
	answer_fifteen = forms.CharField(max_length = 140, required = False)