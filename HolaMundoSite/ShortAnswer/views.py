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

# render success page
@login_required()
def success(request):
	return render(request, 'ShortAnswer/success.html')

# render submit page
@login_required()
def submit(request):
	return render(request, 'ShortAnswer/submit.html')

# results view displays results for user
@login_required()
def results(request, answerID):
	r = Answer.objects.get(answerID=answerID)
	context = {'question': r.question, 'score': r.score, 'total': r.total, 'user': r.user}
	return render(request, 'ShortAnswer/results.html', context)

# create_essay_quiz is a view where the Content Creator can create
# a Short Answer or Essay question to be answered by the Student.
# You must be logged in to the site create a quiz
@login_required()
def create_essay_quiz(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = QuestionForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			# set data from Question Model to q
			q = Question()
			# clean data from Question Model
			q.title = form.cleaned_data["title"]
			q.difficulty = form.cleaned_data["difficulty"]
			q.question = form.cleaned_data["question"]
			q.correctAnswer = form.cleaned_data["correctAnswer"]

			# request author as User
			q.author = request.user
			# save data from Question Model
			q.save()
			return render(request, 'ShortAnswer/success.html')
			#return HttpResponseRedirect('/success.html')
	# if request method is GET, we will create a blank Question form
	elif request.method == 'GET':
		form = QuestionForm()
	# create blank Question Form
	else:
		form = QuestionForm()
	return render(request, 'ShortAnswer/essay_quiz.html', {"form": form})

# take_quiz is a view for the Student to take the Short Answer/Essay
# Quiz. This view will save results to the database and update the 
# User's score if the User is Correct. You must be logged in to the site
# to take the quiz.
@login_required()
def take_quiz(request, questionID):
	# set quiz to objects in Question Model by using primary key questionID
	quiz = Question.objects.get(questionID=questionID)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		a = Answer(question=quiz, user = request.user)
		# set form to AnswerForm by request POST and set a to instance
		form = AnswerForm(request.POST, instance=a)
		# check whether it is valid
		if form.is_valid():
			# save form as a
			a = form.save()
			# set q to objects in Question Model by using primary key questionID
			q = Question.objects.get(questionID=questionID)
			# check to see if User's answer is Correct
			if((q.correctAnswer == a.answer)):
				# update score attribute in a to 100 if correct
				setattr(a, 'score', 100)
				# update total attribute in a to 100
				setattr(a, 'total', 100)
				# save a
				a.save()
				print "Correct"
			# else answer is incorrect
			else:
				# set score attribute in a to 0
				setattr(a, 'score', 0)
				# update total attribute in a to 100
				setattr(a, 'total', 100)
				# save a
				a.save()
				print "Incorrect"
			# a.title = q.title
			# a.user = request.user
			return HttpResponseRedirect('results', a.answerID)
	# if request method is GET, set form to Answer Form
	elif request.method == 'GET':
		print "GET"
		form = AnswerForm()
	# else set form to Answer Form
	else:
		form = AnswerForm()
	# set quiz to objects in Question Model by using primary key questionID
	quiz = Question.objects.get(questionID=questionID)
	# set context to objects in Question Model
	context = {'questionID': quiz.questionID, 'title': quiz.title, 
				'question': quiz.question, 'correctAnswer': quiz.correctAnswer, 
				'difficulty': quiz.difficulty, 'form': form}
	# render request and send to take_quiz.html for ShortAnswer
	return render(request, 'ShortAnswer/take_quiz.html', context)

