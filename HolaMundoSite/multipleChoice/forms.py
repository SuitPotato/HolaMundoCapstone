from django.forms import ModelForm
from django import forms
from multipleChoice.models import Quiz, Response

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'answerA', 'answerB', 'answerC', 'answerD', 'correctAnswer', 'score']
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['title', 'answer', 'score']
