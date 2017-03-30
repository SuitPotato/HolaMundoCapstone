#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm
# Import Models
from ShortAnswer.models import *


# Form for Short Answer/Essay Question
class QuestionForm(forms.ModelForm):
	# Meta Class
    class Meta:
    	# Based off Model: Question
        model = Question
        fields = ('title', 'author', 'question', 'answer', 'correctAnswer')

    # fields defined under forms
	title = forms.CharField(max_length = 140)
	author = forms.CharField(max_length = 140)
	question = forms.CharField(max_length = 500)
	answer = forms.CharField(max_length = 1000)
	correctAnswer = forms.CharField(max_length=1000)

# form for User's Answer to Short Answer/Essay Question
class AnswerForm(forms.ModelForm):
	# Meta Class
	class Meta:
		# Based off Model: Answer
		model = Answer
		fields = {'title', 'answer', 'score'}

	# fields defined under form
	title = forms.CharField(max_length=140)
	answer = forms.CharField(max_length=1000)
	score = forms.CharField(max_length=100)
