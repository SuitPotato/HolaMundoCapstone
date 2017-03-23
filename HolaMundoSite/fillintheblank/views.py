from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from fillintheblank.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
#SHort answer/essay quiz that is created when a user is logged in
@login_required()
def quiz(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return render(request, 'fillintheblank/success.html')
    else:
        form = QuestionForm()
    return render(request, 'fillintheblank/quiz.html', {'form': form})

@login_required()
def answer_question(request):
    if request.method == 'POST':
        form = Answer(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()

    else:
        form = Answer()
        return render(request, 'fillintheblank/answer.html', {'form': form})

@login_required()
def FillInTheBlankQuestion(request):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return render(request, 'fillintheblank/success.html')
    else:
        form = FillInTheBlank()
    return render(request, 'fillintheblank/fb_quiz.html', {'form': form})



    