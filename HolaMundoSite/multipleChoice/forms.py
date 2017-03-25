from django.forms import ModelForm
from django import forms
from multipleChoice.models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'answerA', 'answerB', 'answerC', 'answerD', 'correctAnswer']
