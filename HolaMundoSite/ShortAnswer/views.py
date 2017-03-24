# Django Imports 
from django.shortcuts import render, redirect
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

# view is to see the Short Answer/Essay question
@login_required()
def view_essay_quiz(request, title):
	try:
		question1 = Question.objects.get(questionID__exact = questionID, title = title)
		context = {'title': question1.title, 'question': question1.question,
		 'answer': question1.answer}

		return render(request, 'ShortAnswer/essay_quiz.html', context)
	except:
		return render(request, 'Video_page/404.html')

# Short answer/essay quiz that is created when a user is logged in
@login_required()
def create_essay_quiz(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = QuestionForm(request.POST)

        if form.is_valid():
            question1 = Question()
            question1.title = form.cleaned_data["title"]
            question1.question = form.cleaned_data["question"]
            question1.answer = form. cleaned_data["answer"]
            question1.save()
            return render(request, 'ShortAnswer/success.html')
    elif request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'ShortAnswer/essay_quiz.html', {'form': form})

@login_required
def success(request):
	return render(request, 'ShortAnswer/success.html')

