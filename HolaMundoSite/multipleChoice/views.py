from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from django import forms
from multipleChoice.models import Question
from multipleChoice.forms import (
    QuestionForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quiz(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
    else:
        form = QuestionForm()
    return render(request, 'multipleChoice/quiz.html', {'form': form})

def takeQuiz(request,question):
    # context = RequestContext(request)
    # context_dict = {'question': question}
    # try:
    #     qustion = Question.objects.get(question=question)
    # except:
    #     pass
    try:
        q = Question.objects.get(question=question)
        context = {'question': q.question, 'answer_a': q.answer_a, 'answer_b': q.answer_b, 'answer_c': q.answer_c,
        'answer_d': q.answer_d, 'correct_answer': q.correct_answer}
        return render(request, 'multipleChoice/takeQuiz.html', context)
    except:
        return render(request, 'multipleChoice/quiz.html')
