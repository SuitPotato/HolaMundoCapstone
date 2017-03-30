#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm
# Import Models
from fillintheblank.models import *

# class Create_FillInTheBlank_quiz(forms.Form):

# Form for Fill In The Blank Question
class FillInTheBlank(forms.ModelForm):
	class Meta:
		# Based off Model: Fill In The Blank Question
		model = FillInTheBlankQuestion
		fields = ('author', 'question_start', 'correctAnswer', 'question_end', 'answer')

	# fields defined under forms
	# title = forms.CharField(max_length = 140)
	author = forms.CharField(max_length=100)
	question_start = forms.CharField(max_length = 100)
	correctAnswer = forms.CharField(max_length=100)
	question_end = forms.CharField(max_length = 100)
	answer = forms.CharField(max_length = 100)

# Form for Fill In The Blank Answer
class AnswerForm(forms.ModelForm):
		# Meta Class
	class Meta:
		# Based off Model: Answer
		model = Answer
		fields = {'question', 'answer', 'score'}

	# fields defined under form
	question = forms.CharField(max_length=140)
	answer = forms.CharField(max_length=1000)
	score = forms.IntegerField(max_length=100)