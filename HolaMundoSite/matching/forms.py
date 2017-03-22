from django import forms
from django.forms import ModelForm
from matching.models import *

#form created from model for taking in user input quiz name and number
#of choices in the question
class MatchingNumber(forms.ModelForm):
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
		fields = ['question', 'answer', 'rand_letter',]
	'''MN = MatchingNumber(forms.ModelForm)
	copynumber = MN.number
	temp = 0
	while(temp != copynumber):
		question = forms.CharField(label='Question:')
		answer = forms.CharField(label='Answer')
		rand_letter = forms.CharField(label='Letter')
		temp += 1'''
		
#form created from model that takes in students answer
class MatchingAnswer(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['answer',]
	#user_answer = forms.CharField(label='Your answer:')