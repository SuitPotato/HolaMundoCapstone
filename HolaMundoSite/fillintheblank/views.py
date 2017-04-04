# Django Imports 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django import forms
from django.db import models

# Import Forms
from fillintheblank.forms import *
# Import Models
from fillintheblank.models import *

# Required for importing User for Author
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# render success page
@login_required()
def success(request):
	return render (request, 'fillintheblank/success.html')

# render submit page
@login_required()
def submit(request):
	return render(request, 'fillintheblank/submit.html')

# results view displays results for user
@login_required()
def results(request, answerID):
	quiz = Answer.objects.get(answerID=answerID)
	context = { 'title': quiz.title, 'user': quiz.user, 'score': quiz.score, 'total': quiz.total}
	return render(request, 'ShortAnswer/results.html', context)

# create_quiz is a view that is for Content Creators to create a 
# Fill In The Blank quiz. You must be logged in to the site to 
# create a quiz.
@login_required()
def create_quiz(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = QuestionForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			# set data from Question model to q
			q = Question()
			# clean data from Question Model 
			q.title = form.cleaned_data["title"]
			q.difficulty = form.cleaned_data["difficulty"]
			q.question_start = form.cleaned_data["question_start"]
			q.question_end = form.cleaned_data["question_end"]
			q.correctAnswer = form.cleaned_data["correctAnswer"]

			# request author as User
			q.author = request.user
			# save data from Question Model
			q.save()
			# print "Saved"
			return render(request, 'fillintheblank/success.html')
			#return HttpResponseRedirect('/success/')
	# if request method is GET, we will create a blank Question Form
	elif request.method == 'GET':
		form = QuestionForm()
	# create blank Question Form
	else:
		form = QuestionForm()
	return render(request, 'fillintheblank/fb_quiz.html', {"form": form})

# take_quiz is a view for the Student to take the Fill In The Blank
# Quiz. This view will save results to database and update the User's
# score if the User is Correct. You must be logged in to the site to 
# take the quiz.
@login_required()
def take_quiz(request, questionID):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = AnswerForm(request.POST)
		# check whether it is valid
		if form.is_valid():
			# set q to the Question Model by primary key QuestionID
			q = Question.objects.get(questionID = questionID)
			# set a to data from Answer Model
			a = Answer()
			# clean data from Answer
			a.answer = form.cleaned_data["answer"]
			# check to see if User's answer is Correct
			if((a.answer == q.correctAnswer)):
				# if yes, increment score by 100
				a.score += 100
				a.total = 100
				print "Correct!"
			# else the User's Answer is wrong 
			else:
				# do not increment score
				a.score = 0
				a.total = 100
				print "Incorrect"
			# set title in Answer Model to title in Question Model
			a.title = q.title
			# set answerID in Answer Model to questionID in Question Model
			a.answerID = q.questionID
			# set user in Answer Model to user who is logged in
			a.user = request.user
			# save answer to database
			a.save()
			# redirect 
			return render(request, 'fillintheblank/submit.html')
	# if request method is GET, set form to Answer Form
	elif request.method == 'GET':
		form = AnswerForm()
	# else set form to Answer Form
	else:
		form = AnswerForm()
	try:
		# set quiz to objects in Question Model by using primary key questionID
		quiz = Question.objects.get(questionID = questionID)
		# # get answer field from Answer model
		# answer_quiz = Answer.objects.get(answer=answer)
		# set context to objects in Question Model
		context = { 'title': quiz.title, 'questionID': quiz.questionID,'user': quiz.user,
					'question_start': quiz.question_start, 'question_end': quiz.question_end,
					'correctAnswer': quiz.correctAnswer, 'difficulty': quiz.difficulty,
					'form': form}
		return render(request, 'fillintheblank/take_quiz.html', context)

	except:
		return HttpResponseRedirect('http://www.djangoproject.com')

