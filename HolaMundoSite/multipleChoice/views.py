from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from django import forms
from multipleChoice.models import Quiz
from multipleChoice.forms import (
    QuizForm
  )
from django.contrib.auth.decorators import login_required

# Create your views here.
def results(request):
    # show results of quiz to user
    return redirect('https://www.google.de/')

def view_takeQuiz(request,quizID):
    try:
        quiz = Quiz.objects.get(quizID=quizID)
        context = {'title': quiz.title, 'answerA': quiz.answerA, 'answerB': quiz.answerB,
        'answerC': quiz.answerC,'answerD': quiz.answerD,
        'correctAnswer': quiz.correctAnswer, 'score':quiz.score}
        ctx = {}
        if request.method == 'POST' and 'input' in request.POST:
           ctx['score'] = int(request.get('input', 0)) + 1
           return render(request, 'multipleChoice/takeQuiz.html', score)
        return render(request, 'multipleChoice/takeQuiz.html', context)


    except:
        return render(request, 'multipleChoice/quiz.html', {})

@login_required
def quiz(request):
    if request.method == 'POST':
       form = QuizForm(request.POST)
       if form.is_valid():
          q = Quiz()
          q.title = form.cleaned_data["title"]
          q.answerA = form.cleaned_data["answerA"]
          q.answerB = form.cleaned_data["answerB"]
          q.answerC = form.cleaned_data["answerC"]
          q.answerD = form.cleaned_data["answerD"]
          q.correctAnswer = form.cleaned_data["correctAnswer"]
          q.save()
        #   fix this
          return HttpResponseRedirect('/success/')
    elif request.method == 'GET':
         form = QuizForm()
    else:
       form = QuizForm()
    return render(request, 'multipleChoice/quiz.html', {"form":form})
