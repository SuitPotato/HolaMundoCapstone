# Django Imports 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models

# Import Forms
from fillintheblank.forms import *

# Required for importing User for Author
from django.contrib.auth.decorators import login_required

# Create your views here.

#Short answer/essay quiz that is created when a user is logged in
@login_required()
def essay_quiz(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            # save the variable into the model.
            question.save()
            return render(request, 'fillintheblank/success.html')
    else:
        form = QuestionForm()
    return render(request, 'fillintheblank/essay_quiz.html', {'form': form})

# The answer_question view is for the student to complete the question being asked
# and subitting their answer
@login_required()
def answer_question(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = Answer(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # save the variable into the model.
            answer.save()

    else:
        form = Answer()
        return render(request, 'fillintheblank/essay_answer.html', {'form': form})

# This view retireves the form for Fill In The Blank question for the teacher
# to create a question for a fill in the blank question.
@login_required()
def FillInTheBlankQuestion(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = FillInTheBlank(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            # Save the variable into the model.
            question.save()
            return render(request, 'fillintheblank/success.html')
    else:
        form = FillInTheBlank()
    return render(request, 'fillintheblank/fb_quiz.html', {'form': form})

