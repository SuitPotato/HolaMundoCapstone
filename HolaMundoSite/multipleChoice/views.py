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
def view_takeQuiz(request,title):
    # try:
        # sentence = Sentence.objects.get(title = title)
        # form = QuestionForm()
        # quiz = Quiz(question='test', answerA='test', answerB='test', answerC='test',answerD='test', correctAnswer='test')
        # quiz.save()
        quiz = Quiz.objects.get(title="test")
        # myquest = Question.objects.all()
        context = {'title': quiz.title, 'answerA': quiz.answerA, 'answerB': quiz.answerB,
                   'answerC': quiz.answerC,'answerD': quiz.answerD,
                   'correctAnswer': quiz.correctAnswer}
        return render(request, 'multipleChoice/takeQuiz.html', context)
    # except:
    #     return render(request, 'multipleChoice/quiz.html', {})

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
