#Django Imports
from django import forms
from django.forms import ModelForm
# Import Models
from fillintheblank.models import *

# class Create_FillInTheBlank_quiz(forms.Form):

# Form for Short Answer/Essay Question
class QuestionForm(forms.ModelForm):
	# Meta Class
    class Meta:
    	# Based off Model: Question
        model = Question
        fields = ('question', 'answer', 'key')

# Form for Answer
class Answer(forms.ModelForm):
	# Meta Class
	class Meta:
		# Based off Model: Answer
		model = Answer
		fields = ('answer', )

# Form for Fill In The Blank Question
class FillInTheBlank(forms.ModelForm):
	class Meta:
		# Based off Model: Fill In The Blank Question
		model = FillInTheBlankQuestion
		fields = ('question_start', 'question_end', 'answer', 'key')