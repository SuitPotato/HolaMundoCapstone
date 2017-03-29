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

# Create your views here.
# # view to take in score and update database model
def submit(request):
    r = Response()
    r.title = "test"
    # if request.method == 'POST':
    #    r.answer = request.POST['A']
    r.save()
    return redirect('http://stackoverflow.com')
    # #  if request.method == 'POST':
    #     form = ResponseForm(data=request.POST, instance=quiz)
    #     if form.is_valid():
    #        r = Response()
    #        r.title = request.POST.get("title")
    #        r.answer = request.POST.get("answer")
    #        r.score = request.POST.get("score")
    #        r.save()
    #  return render(request, 'multipleChoice/submit.html', {})

def view_takeQuiz(request,quizID):
    try:
        quiz = Quiz.objects.get(quizID=quizID)
        context = {'title': quiz.title, 'answerA': quiz.answerA, 'answerB': quiz.answerB,
        'answerC': quiz.answerC,'answerD': quiz.answerD,
        'correctAnswer': quiz.correctAnswer, 'score': quiz.score}
        return render(request, 'multipleChoice/takeQuiz.html', context)
        context = RequestContext(request)
        if request.method == 'POST':
           form = RequestForm(request)
           if form.is_valid():
              form.save(commit=True)
              return submit(request)
           else:
              print form.errors
        else:
            form = RequestForm()
        return redirect('http://www.tangowithdjango.com')
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
