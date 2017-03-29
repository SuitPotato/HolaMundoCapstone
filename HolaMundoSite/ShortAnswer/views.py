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
            # set data from form and set to cleaned data
            quiz = Question()
            quiz.title = form.cleaned_data["title"]
            quiz.question = form.cleaned_data["question"]
            #quiz.answer = form.cleaned_data["answer"]
            quiz.correctAnswer = form.cleaned_data["correctAnswer"]
            # save data
            quiz.save()
            # render to success page of creating a quiz
            return render(request, 'ShortAnswer/success.html')
    elif request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'ShortAnswer/essay_quiz.html', {'form': form})

# View is to display for User to take quiz
@login_required()
def take_quiz(request, questionID):
    try:
        # set quiz by calling Question model and using questionID to
        # get specific information.
        quiz = Question.objects.get(questionID=quuestionID)
        context = {'title': quiz.title, 'question': quiz.question, 'answer': quiz.answer,
                'score': quiz.score}
                #{'correctAnswer': quiz.correctAnswer,}
        return render(request, 'ShortAnswer/take_quiz.html', context)
        
    except:
        return render(request, 'ShortAnswer/essay_quiz.html', {})


# View is to display results
@login_required()
def results(request, questionID):
    # get question from Question Model
    quiz = get_object_or_404(Question, pk=questionID)
    # context of Question Model
    context = {'title': quiz.title, 'question': quiz.question, 'answer': quiz.answer,
                    'correctAnswer': quiz.correctAnswer}
    # display results page 
    return render(request, 'ShortAnswer/results.html', context)


# view to save User's answer and update in database
@login_required()
def submit(request):
    if request.method == 'POST':
        #  if User wants to submit answers, display answer form
        form = AnswerForm()

        if form.is_valid():
            # set data from Answer Model
            a = Answer()
            a.title = request.POST.get("title")
            a.answer = request.POST.get("answer")
            a.score = request.POST.get("score")
            # save data
            a.save()
            # Not sure where to send Users
            return HttpResponseRedirect('ShortAnswer/success.html')
        elif request.method == 'GET':
            form = AnswerForm()
        else:
            form = AnswerForm()
            return redirect('https://djangoproject.com')
'''
@login_required()
def success(request):
	return render(request, 'ShortAnswer/success.html')

'''