#Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm
# Import Models
from ShortAnswer.models import *

# class Create_FillInTheBlank_quiz(forms.Form):

# Form for Short Answer/Essay Question
class QuestionForm(forms.ModelForm):
	# Meta Class
    class Meta:
    	# Based off Model: Question
        model = Question
        fields = ('title', 'author', 'question_name', 'answer')

    # fields defined under forms
	title = forms.CharField(max_length = 140)
	author = forms.CharField(max_length = 140)
	question_name = forms.CharField(max_length = 500)
	answer = forms.CharField(max_length = 1000)
