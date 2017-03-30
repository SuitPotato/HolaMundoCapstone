from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from django import forms
from multipleChoice.models import Quiz, Response
from multipleChoice.forms import (
    QuizForm, ResponseForm
  )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# view to bring up quiz for user
def view_takeQuiz(request,quizID):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        # print "POST"
        if form.is_valid():
            q = Quiz.objects.get(quizID=quizID)
            r = Response()
            #r.title = form.cleaned_data["title"]
            r.answer = form.cleaned_data["answer"]
            #r.score = form.cleaned_data["score"]
            # if the user submits correct answer, increment score by 1
            if((r.answer == q.correctAnswer)):
                r.score = 1
                print "Correct!"
            else:
                # if they guess wrong, set equal to zero
                r.score = 0
                print "Not correct!"
            # save form
            r.save()
            # change redirect in UI phase
            return redirect('https://www.djangoproject.com/')
        elif request.method == 'GET':
            form = ResponseForm()
        else:
            form = ResponseForm()
    try:
        quiz = Quiz.objects.get(quizID=quizID)
        context = {'title': quiz.title, 'answerA': quiz.answerA, 'answerB': quiz.answerB,
        'answerC': quiz.answerC,'answerD': quiz.answerD,
        'correctAnswer': quiz.correctAnswer, 'score': quiz.score, 'form': form}
        return render(request, 'multipleChoice/takeQuiz.html', context)

    except:
        return render(request, 'multipleChoice/quiz.html')


@login_required
# view to create a quiz
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
