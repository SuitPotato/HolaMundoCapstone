#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm
# Import Models
from ShortAnswer.models import *


# Form for Short Answer/Essay Question
class QuestionForm(forms.Form):
	# Meta Class
    class Meta:
    	# Based off Model: Question
        model = Question
        fields = ['question', 'correctAnswer']

    # fields defined under forms
	question = forms.CharField(max_length = 1000)
	correctAnswer = forms.CharField(max_length=1000)

# form for User's Answer to Short Answer/Essay Question
class AnswerForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off Model: Answer
		model = Answer
		fields = ['answer']

	# fields defined under form
	#question = forms.CharField(max_length=140)
	answer = forms.CharField(max_length=1000)
	#score = forms.CharField(max_length=100)
