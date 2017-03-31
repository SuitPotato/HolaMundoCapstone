#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm
# Import Models
from fillintheblank.models import *

# Form for Fill In The Blank Question
class QuestionForm(forms.Form):
	class Meta:
		# Based off Model: Fill In The Blank Question
		model = Question
		fields = ('title', 'difficulty', 'question_start', 'correctAnswer', 'question_end')

	# Choices: DIFFICULTIES
	DIFFICULTIES = (
		('Beginner', '1'),
		('Intermediate', '2'),
		('Advanced', '3'),
		)

	# fields defined under form
	title = forms.CharField(max_length = 50)
	difficulty = models.ChoiceField(choices = DIFFICULTIES)
	question_start = forms.CharField(max_length = 100)
	correctAnswer = froms.CharField(max_length = 100)
	question_end = forms.CharField(max_length = 100)

# Form for Fill In The Blank Answer
class AnswerForm(forms.Form):
	# Based off Model: Fill In The Blank Answer
	class Meta:
		model = Answer
		fields = ('answer')

	# fields defined under form
	answer = forms.CharField(max_length = 100)
