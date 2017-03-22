from django import forms
from django.forms import ModelForm
from fillintheblank.models import Question

# class Create_FillInTheBlank_quiz(forms.Form):

class QuestionForm(forms.ModelForm):
	#question = forms.CharField(label='Question:')
	#answer = forms.CharField(label='Answer:')

    #template_name = '/fillintheblank/fb_quiz'
    class Meta:
        model = Question
        fields = ('question', 'answer', 'key')
