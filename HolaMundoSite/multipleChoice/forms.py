from django.forms import ModelForm
from django import forms
from multipleChoice.models import Quiz

class QuizForm(forms.ModelForm):
 # template_name = '/multipleChoice/quiz'
 # class Meta:
 #     model = Question
 #     fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')
    class Meta:
        model = Quiz
        fields = ['title', 'answerA', 'answerB', 'answerC', 'answerD', 'correctAnswer']
