#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm, Textarea
# Import Models 
from ShortAnswer.models import *

# Form for Short Answer/Essay Question
class QuestionForm(forms.Form):
	class Meta:
		# Based off Model: Short Answer/Essay Question
		model = Question 
		fields = ('title', 'difficulty', 'question', 'correctAnswer')

	# Choices: DIFFICULTIES
	DIFFICULTIES = (
		('1', 'Beginner'),
		('2', 'Intermediate'),
		('3', 'Advanced'),
		)

	# fields defined under form
	title = forms.CharField(max_length = 50)
	difficulty = forms.ChoiceField(choices = DIFFICULTIES)
	question = forms.CharField(max_length = 100, 
				widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}))
	correctAnswer = forms.CharField(max_length = 1000, 
				widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}))

# Form for Short Answer/Essay Answer
class AnswerForm(ModelForm):
	class Meta:
		# Based off Model: Short Answer/Essay Answer
		model = Answer 
		fields = ['answer',]
		widgets = {'answer': Textarea(attrs={'cols': 30, 'rows': 3}),
				}

	# fields defined under form
	# answer = forms.CharField(max_length = 1000)
