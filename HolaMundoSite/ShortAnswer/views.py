# Django Imports 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User


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
        form = QuestionForm(request.POST)
         
        if form.is_valid():
            q = Question()
            q.question = form.cleaned_data["question"]
            q.correctAnswer = form.cleaned_data["correctAnswer"]
            q.save()
            return render(request, 'ShortAnswer/success.html')
    elif request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'ShortAnswer/essay_quiz.html', {'form': form})

'''
        # Form is a variable that contains the source form
        form = QuestionForm(request.POST)

        if form.is_valid():
            # set data from form and set to cleaned data
            quiz = Question()
            #quiz.title = form.cleaned_data["title"]
            #quiz.author = form.cleaned_data["author"]
            quiz.question = form["question"]
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
    '''
# View is to display for User to take quiz
@login_required()
def take_quiz(request, questionID):
    if request.method == 'POST':
        # form for Answer form 
        form = AnswerForm(request.POST)

        if form.is_valid():
            # set q to the objects in Question Model
            q = Question.objects.get(questionID = questionID)
            # set a to Answer Model
            a = Answer()
            a.answer = form.cleaned_data["answer"]
            print a.answer

            # check if answer is correct
            if(( a.answer == q.correctAnswer )):
                # increase score by 1
                a.score = 1
                print "Correct"
            # else answer is wrong
            else:
                # keep score at 0
                a.score = 0
                print "Incorrect"
            # save answer
            a.save()
            # redirect to success page
            return HttpResponseRedirect('ShortAnswer/success.html')
        else:
            print "Form is invalid"
    # Get answer form if request method is GET
    elif request.method == 'GET':
        form = AnswerForm()
    # set form to Answer Form
    else:
        form = AnswerForm()

    try:
        # set quiz by calling Question model and using questionID to
        # get specific information.
        quiz = Question.objects.get(questionID=questionID)
        context = {'question': quiz.question,
                'correctAnswer': quiz.correctAnswer, 'form': form}
        return render(request, 'ShortAnswer/take_quiz.html', context)
        # context = RequestContext(request)

        # if request.method == 'POST':
        #    form = RequestForm(request)
        #    if form.is_valid():
        #        form.save(commit=True)
        #        return submit(request)
        #    else:
        #        print form.errors
        # else:
         #   form = RequestForm()
          #  return redirect('http://www.djangoproject.com')
        
    except:
        return render(request, 'ShortAnswer/essay_quiz.html', {})

@login_required()
def success(request):
    return render(request, 'ShortAnswer/success.html')

'''
# view to save User's answer and update in database
@login_required()
def submit(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            # get all objects in Question Model
            quiz = Question.objects.get(questionID=questionID)

            a = Answer()
            a.title = form.cleaned_data["title"]
            a.answer = form.cleaned_data["author"]
            a.score = form.cleaned_data["score"]

            # compare Student's Answer to Correct Answer
            if (a.answer == quiz.correctAnswer):
                a.score = 1
                print "Correct"

            else:
                a.score = 0
                print "Incorrect"
            a.save()
            return redirect('http://www.stackoverflow.com')
    elif request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm()
    return render(request, 'ShortAnswer/submit.html', {"form":form})



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

@login_required()
def success(request):
	return render(request, 'ShortAnswer/success.html')

'''