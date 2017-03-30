# Django Imports 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models

# Import Forms
from fillintheblank.forms import *
# Import Models
from fillintheblank.models import *

# Required for importing User for Author
from django.contrib.auth.decorators import login_required

# View is for taking quiz for the User
@login_required()
def view_quiz(request, questionID):
    if request.method == 'POST':
        # form for Answer Form
        form = AnswerForm(request.POST)

        if form.is_valid():
            #set q to the objects in FillInTheBlankQuestion Model
            q = FillInTheBlankQuestion.objects.get(questionID = questionID)
            #set a to Answer Model
            a = Answer()
            a.answer = form.cleaned_data["answer"]

            # check if answe is correct
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
            #redirect to success page
            return HttpResponseRedirect('fillintheblank/success.html')
    # Get answer form if request method is GET
    elif request.method == 'GET':
        form = AnswerForm()
    # set form to Answer Form
    else:
        form = AnswerForm()

    try:
         # set quiz by calling FillInTheBlankQuestion model and using questionID 
         # to get specific information.
        quiz = FillInTheBlankQuestion.objects.get(questionID=questionID)
        context = {'question_start': quiz.question_start,
                    'answer': quiz.answer, 'question_end': quiz.question_end,
                    'correctAnswer': quiz.correctAnswer, 'form': form}

        return render(request, 'fillintheblank/take_quiz.html', context)
    except:
        return render(request, 'fillintheblank/fb_quiz.html', {})


# This view retireves the form for Fill In The Blank question for the teacher
# to create a question for a fill in the blank question.
@login_required()
def create_quiz(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = FillInTheBlank(request.POST)

        if form.is_valid():
            # set data from form and set to cleaned data
            quiz = FillInTheBlankQuestion()
            #quiz.title = form.cleaned_data["title"]
            quiz.author = form.cleaned_data["author"]
            quiz.question_start = form.cleaned_data["question_start"]
            quiz.answer = form.cleaned_data["answer"]
            quiz.question_end = form.cleaned_data["question_end"]
            quiz.correctAnswer = form.cleaned_data["correctAnswer"]
            
            # Save the variable into the model.
            quiz.save()

            return render(request, 'fillintheblank/success.html')

    elif request.method == 'GET':
        form = FillInTheBlank()
    else:
        form = FillInTheBlank()
    return render(request, 'fillintheblank/fb_quiz.html', {'form': form})

@login_required()
def success(request):
    return render(request, 'fillintheblank/success.html')

'''
# view to save User's answer and update in database
@login_required()
def submit(request):
    if request.method == 'POST':
        form = AnswerForm()

        if form.is_valid():
            a = Answer()
            a.title = request.POST.get("title")
            a.answer = request.POST.get("answer")
            a.score = request.POST.get("score")
            a.save()
            return HttpResponseRedirect('fillintheblank/success.html')
        elif request.method == 'GET':
            form = AnswerForm()
        else:
            form = AnswerForm()
            return redirect('https://djangoproject.com')

# view is to display results
@login_required()
def results(request, questionID):
    # get question from Question Model
    question = get_object_or_404(FillInTheBlankQuestion, pk=questionID)
    # context of Question Model
    context = {'title':quiz.title, 'author': question.author , 
                'question_start': quiz.question_start,'question_end': quiz.question_end,
                'correctAnswer': quiz.correctAnswer }
    return render(request, 'fillintheblank/results.html', context)
'''
