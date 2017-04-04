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
	quiz = Question.objects.get(questionID=questionID)
	if request.method == 'POST':
		print "POST"
		a = Answer(question=quiz, user = request.user)
		print a
		form = AnswerForm(request.POST, instance=a)
		if form.is_valid():
			print "Valid"
			a = form.save()
			print a.answer
			q = Question.objects.get(questionID=questionID)
			if((q.correctAnswer == a.answer)):
				setattr(a, 'score', 100)
				setattr(a, 'total', 100)
				a.save()
				print "Correct"
			else:
				setattr(a, 'score', 0)
				setattr(a, 'total', 100)
				a.save()
				print "Incorrect"
			# a.title = q.title
			# a.user = request.user
			return HttpResponseRedirect('results', a.answerID)
	elif request.method == 'GET':
		print "GET"
		form = AnswerForm()
		print form
	else:
		form = AnswerForm()

	quiz = Question.objects.get(questionID=questionID)
	print quiz
	context = {'questionID': quiz.questionID, 'title': quiz.title, 
				'question': quiz.question, 'correctAnswer': quiz.correctAnswer, 
				'difficulty': quiz.difficulty, 'form': form}
	return render(request, 'ShortAnswer/take_quiz.html', context)

		# return HttpResponseRedirect('http://www.djangoproject.com')

'''
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = AnswerForm(request.POST)
		# check whether it's valid
		if form.is_valid():
			# set q to the Question Model by primary key questionID
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
				print "Correct"
			# else the User's answer is Incorrect
			else:
				# do not increment score
				a.score = 0
				a.total = 100
				print "Incorrect"
			# set title in Answer Model to title in Question Model
			a.title = q.title
			# set answerID in Answer Model to questionID in Question Model
			# a.answerID = q.questionID
			# set user in Answer Model to user who is logged in
			a.user = request.user
			# save answer to the database
			a.save()
			# redirect
			return render(request, 'ShortAnswer/submit.html')
		# if request method is GET, set form to Answer Form
		elif request.method == 'GET':
			form = AnswerForm()
		# else set form to Answer Form
		else:
			form = AnswerForm()
	try:
		# set quiz to objects in Question Model by using primary key questionID
		quiz = Question.objects.get(questionID = questionID)
		# set context to objects in Question Model
		context = {'title': quiz.title, 'questionID': quiz.questionID,
					'question': quiz.question, 'user': quiz.user, 'correctAnswer': quiz.correctAnswer,
					'difficulty': quiz.difficulty,
				}
		return render(request, 'ShortAnswer/take_quiz.html')

	except:
		#return render(request, 'ShortAnswer/essay_quiz.html')
		return HttpResponseRedirect('http://www.djangoproject.com')
	'''
