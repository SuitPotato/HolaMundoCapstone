from django import forms
from django.db import models
from django.forms import ModelForm
from matching.models import *

#form created from model for taking in user input quiz name and number
#of choices in the question
'''class MatchingNumber(forms.ModelForm):
	class Meta:
		model = Number
		fields = ['quiz_name', 'number',]
	#quiz_name = forms.CharField(label='Quiz Name')
	#number = forms.IntegerField(label='How many matching questions do you want?', max_value=26, min_value=2)

#form created from model for taking in user input choices, answers,
#and corresponding letter for answer for matching that the student
#can input	
class MatchingQuestion(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question', 'correct', 'rand_letter',]
		
#form created from model that takes in students answer
class MatchingAnswer(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['answer',]
	#user_answer = forms.CharField(label='Your answer:')'''
	
class NumberForm(ModelForm):
	class Meta:
		model = Matching
		fields = ['options']
	
	NUMBER_OPTIONS = (
	('2', '2'),
	('3','3'),
	('4', '4'),
	)
	
	#title = forms.CharField(max_length = 140)
	
	#options = forms.CharField(max_length=2)
	
	
class MatchingForm(forms.Form):
	class Meta:
		# Based off of the models
		model = Matching
		# Add options
		fields = ['title', 'quizID', 'left_one','left_two','left_three','left_four','right_one',
				'right_two','right_three','right_four',]
		
	# Fields defined under forms.
	
	title = forms.CharField(max_length = 140)
	
	#quizID = forms.IntegerField(widget = forms.HiddenInput(), required = True)
	
	left_one = forms.CharField(max_length = 140)
	left_two = forms.CharField(max_length = 140)
	left_three = forms.CharField(max_length = 140)
	left_four = forms.CharField(max_length = 140)
	
	right_one = forms.CharField(max_length = 140)
	right_two = forms.CharField(max_length = 140)
	right_three = forms.CharField(max_length = 140)
	right_four = forms.CharField(max_length = 140)
	
class AnswerForm(forms.Form):
	class Meta:
		model = Answer
		fields = ['answer_one', 'answer_two', 'answer_three',
				'answer_four']
	answer_one = forms.CharField(max_length = 140)
	answer_two = forms.CharField(max_length = 140)
	answer_three = forms.CharField(max_length = 140)
	answer_four = forms.CharField(max_length = 140)