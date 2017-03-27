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
		fields = ('title', 'question_start', 'question_end', 'answer', 'correctAnswer')

	# fields defined under forms
	title = forms.CharField(max_length = 140)
	question_start = forms.CharField(max_length = 100)
	question_end = forms.CharField(max_length = 100)
	answer = forms.CharField(max_length = 100)
	correctAnswer = forms.CharField(max_length=100)