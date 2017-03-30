from django.forms import ModelForm
from django import forms
from multipleChoice.models import Quiz, Response

class QuizForm(forms.Form):
    class Meta:
        model = Quiz
        fields = ['title', 'answerA', 'answerB', 'answerC', 'answerD', 'correctAnswer', 'score']

    title = forms.CharField(max_length=1500)
    answerA = forms.CharField(max_length=150)
    answerB = forms.CharField(max_length=150)
    answerC = forms.CharField(max_length=150)
    answerD = forms.CharField(max_length=150)
    score = forms.CharField(max_length=150)
    correctAnswer = forms.CharField(max_length=150)
class ResponseForm(forms.Form):
    class Meta:
        model = Response
        #fields = ['title', 'answer', 'score']
        fields = ['answer']
    #title = forms.CharField(max_length=120)
    answer = forms.CharField(max_length=120)
    #score = forms.CharField(max_length=120)
