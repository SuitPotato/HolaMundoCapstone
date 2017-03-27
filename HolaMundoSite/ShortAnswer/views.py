# Django Imports 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models

# Import Forms
from ShortAnswer.forms import *
# Import Models
from ShortAnswer.models import *

# Required for importing User for Author
from django.contrib.auth.decorators import login_required

# Create your views here.

# Short answer/essay quiz that is created when a user is logged in
@login_required()
def create_essay_quiz(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = QuestionForm(request.POST)

        if form.is_valid():
            quiz = Question()
            quiz.title = form.cleaned_data["title"]
            quiz.question = form.cleaned_data["question"]
            quiz.answer = form.cleaned_data["answer"]
            quiz.correctAnswer = form.cleaned_data["correctAnswer"]
            quiz.save()
            return render(request, 'ShortAnswer/success.html')
    elif request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'ShortAnswer/essay_quiz.html', {'form': form})

@login_required()
def take_quiz(request, quizID):
    try:
        quiz = Question.objects.get(quizID=quizID)
        context = {'title': quiz.title, 'question': quiz.question, 'answer': quiz.answer,
                    'correctAnswer': quiz.correctAnswer}
        if request.method == 'GET':
            #return render(request, 'ShortAnswer/results.html', {})
            return render(request, 'ShortAnswer/take_quiz.html', context)
    except:
        return render(request, 'ShortAnswer/essay_quiz.html', {})

@login_required()
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ShortAnswer/results.html', {'question': question})

@login_required()
def success(request):
	return render(request, 'ShortAnswer/success.html')

