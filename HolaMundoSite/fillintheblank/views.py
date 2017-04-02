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

# Create your views here.

# create_quiz is a view that is for Content Creators to create a 
# Fill In The Blank quiz. You must be logged in to the site to 
# create a quiz.
@login_required()
def create_quiz(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)

		if form.is_valid():
			q = Question()
			q.title = form.cleaned_data["title"]
			q.difficulty = form.cleaned_data["difficulty"]
			q.question_start = form.cleaned_data["question_start"]
			q.question_end = form.cleaned_data["question_end"]
			q.correctAnswer = form.cleaned_data["correctAnswer"]

			q.save()
			print "Saved"
			# return render(request, 'fillintheblank/success.html')
			return HttpResponseRedirect('/success/')

	elif request.method == 'GET':
		form = QuestionForm()
	else:
		form = QuestionForm()
	return render(request, 'fillintheblank/fb_quiz.html', {"form": form})

# take_quiz is a view for the Student to take the Fill In The Blank
# Quiz. This view will save results to database and update the User's
# score if the User is Correct. You must be logged in to the site to 
# take the quiz.
@login_required()
def take_quiz(request, questionID):
	if request.method == 'POST':
		form = AnswerForm(request.POST)

		if form.is_valid():
			q = Question.objects.get(questionID = questionID)
			a = Answer()
			a.answer = form.cleaned_data["answer"]
			# check to see if User's answer is Correct
			if((a.answer == q.correctAnswer)):
				# if yes, increment score by 1
				a.score += 1
				print "Correct!"
			# else the User's Answer is wrong 
			else:
				# do not increment score
				a.score = 0
				print "Incorrect"
			# save answer to database
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
		context = { 'title': quiz.title, 'questionID': quiz.questionID,
					'question_start': quiz.question_start, 'question_end': quiz.question_end,
					'correctAnswer': quiz.correctAnswer, 'difficulty': quiz.difficulty,
					}
		return render(request, 'fillintheblank/take_quiz.html', context)

	except:
		return render(request, 'fillintheblank/fb_quiz.html')

