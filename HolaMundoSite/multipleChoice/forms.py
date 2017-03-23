from django.forms import ModelForm
from django import forms
from multipleChoice.models import Question

class QuestionForm(forms.ModelForm):
 # template_name = '/multipleChoice/quiz'
 # class Meta:
 #     model = Question
 #     fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')
    class Meta:
        model = Question
        fields = ['question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'correct_answer']
