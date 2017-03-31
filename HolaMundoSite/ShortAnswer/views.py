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

# create_essay_quiz is a view where the Content Creator can create
# a Short Answer or Essay question to be answered by the Student.
# You must be logged in to the site create a quiz
@login_required()
def create_essay_quiz(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)

		if form.is_valid():
			q = Question()
			q.title = form.cleaned_data["title"]
			q.difficulty = form.cleaned_data["difficulty"]
			q.question = form.cleaned_data["question"]
			q.correctAnswer = form.cleaned_data["correctAnswer"]

			q.save()
			# return render(request, 'ShortAnswer/success.html')
			return HttpResponseRedirect('ShortAnswer/success.html')

	elif request.method == 'GET':
		form = QuestionForm()
	else:
		form = QuestionForm()
	return render(request, 'ShortAnswer/essay_quiz.html', {"form": form})

# take_quiz is a view for the Student to take the Short Answer/Essay
# Quiz. This view will save results to the database and update the 
# User's score if the User is Correct. You must be logged in to the site
# to take the quiz.
@login_required()
def take_quiz(request, questionID):
	if request.method == 'POST':
		form = AnswerForm(request.POST)

		if form.is_valid():
			q = Question.objects.get(questionID = questionID)
			a = Answer()
			a.answer = form.cleaned_data["answer"]
			# check to see if User's answer is Correct
			if((a.asnwer == q.correctAnswer)):
				# if yes, increment score by 1
				a.score = 1
				print "Correct"
			# else the User's answer is Incorrect
			else:
				# do not increment score
				a.score = 0
				print "Incorrect"
			# save answer to the database
			a.save()
			# redirect
			return redirect('https://www.djangoproject.com/')
	# if request method is GET, set form to Answer Form
	elif request.method == 'GET':
		form = AnswerForm()
	# else set form to Answer Form
	else:
		form = AnswerForm()
	try:
		quiz = Question.objects.get(questionID = questionID)
		context = {'title': quiz.title, 'questionID': quiz.questionID,
					'question': quiz.question, 'correctAnswer': quiz.correctAnswer,
					'difficulty': quiz.difficulty,
				}
		return render(request, 'ShortAnswer/take_quiz.html', context)

	except:
		return render(request, 'ShortAnswer/essay_quiz.html')
