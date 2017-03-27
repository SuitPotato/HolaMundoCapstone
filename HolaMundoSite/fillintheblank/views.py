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

@login_required()
def view_quiz(request, title):
    try:
        quiz = FillInTheBlankQuestion.objects.get(title=title)
        context = {'title':quiz.title, 'question_start': quiz.question_start,
                    'answer': quiz.answer, 'question_end': quiz.question_end,
                    'correctAnswer': quiz.correctAnswer }
        if request.method == 'GET':
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
            quiz = FillInTheBlankQuestion()
            quiz.title = form.cleaned_data["title"]
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
def results(request, questionID):
    question = get_object_or_404(FillInTheBlankQuestion, pk=questionID)
    return render(request, 'fillintheblank/results.html', {'question': question})
