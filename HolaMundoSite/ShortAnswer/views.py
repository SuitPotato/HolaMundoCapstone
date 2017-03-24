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
		question = Question.objects.get(title = title)
		context = {'title': question.title, 'question': question.question_name,
		 'answer': question.answer}

		return render(request, 'ShortAnswer/essay_quiz.html', context)
	except:
		return render(request, 'Video_page/404.html')

# Short answer/essay quiz that is created when a user is logged in
@login_required()
def essay_quiz(request):
    if request.method == 'POST':
        # Form is a variable that contains the source form
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = Question()
            question.title = form.cleaned_data["title"]
            question.question_name = form.cleaned_data["question_name"]
            question.answer = form. cleaned_data["answer"]
            question.save()
            return render(request, 'ShortAnswer/success.html')
    elif request.method == 'GET':
        form = QuestionForm()
    else:
        form = QuestionForm()
    return render(request, 'ShortAnswer/essay_quiz.html', {'form': form})

@login_required
def success(request):
	return render(request, 'ShortAnswer/success.html')