from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.decorators import login_required
from matching.models import *
from matching.forms import *
from django.contrib.auth.models import User

#This funciton asks user for the name of their quiz and the nuber of
#choices in their matching question

#login required refers to a user having to be logged in to be able to
#access the following content on all functions in the views file
#where it is located
'''@login_required()
def get_number(request):
	#if the request is post which means you have already completed
	#a form and want to submit it this if statement gets called
	if request.method == 'POST':
		#creates vairable form setting it equal to the completed
		#matching number form from the forms file
		form = MatchingNumber(request.POST)
		if form.is_valid():
			questionnumber = form.save(commit=False)
			questionnumber.save()
			#if all input is vlaid the user should be redirected to
			#the page where they can create their question
			return render(request, '/matching/question.html')
	#if the request isn't post then the page is just being visited
	else:
		#if page is just being visited then we generate the form
		#without posting anthing
		form = MatchingNumber()
	#renders the user request, the html file corresponding to the form
	#and the form itself
	return render(request, 'matching/number.html', {'form': form})
	
#This function lets the user create the question, the corresponding
#answer and a letter to represent the answer for matching
@login_required()		
def get_questions(request):
	if request.method == 'POST':
		form = MatchingQuestion(request.POST)
		if form.is_valid():
			questions = form.save(commit=False)
			questions.save()
			#after successful question creation the user will
			#be redirected to...
			#return HttpResponseRedirect('/completion/')
	else:
		form = MatchingQuestion()
	return render(request, 'matching/question.html', {'form': form})

#this function is a view for the student to be able to take the
#quiz created by the instructor
@login_required()		
def answer_question(request):
	if request.method == 'POST':
		form = MatchingAnswer(request.POST)
		if form.is_valid():
			answers = form.save(commit=False)
			answers.save()
			#The student when submitting his answer will either be redirected
			#to the next part of the course or a page that shows their
			#results from the quiz just taken
			#return HttpResponseRedirect('/completion/')
	else:
		form = MatchingAnswer()
	return render(request, 'matching/answer.html', {'form': form})'''
	
@login_required()
def create_matching(request):
	if request.method == 'POST':
		# Form is a variable that contains the source form
		form = MatchingForm(request.POST)
		if form.is_valid():
			# Specifically calling the model
			v = Matching()
			v.title = form.cleaned_data["title"]
			
			v.left_one = form.cleaned_data["left_one"]
			v.left_two = form.cleaned_data["left_two"]
			v.left_three = form.cleaned_data["left_three"]
			v.left_four = form.cleaned_data["left_four"]
			
			v.right_one = form.cleaned_data["right_one"]
			v.right_two = form.cleaned_data["right_two"]
			v.right_three = form.cleaned_data["right_three"]
			v.right_four = form.cleaned_data["right_four"]
			
			
			# Must save the variables into the model
			v.save()
			
			# HttpResponseRedirect has a view and URL
			return HttpResponseRedirect('/complete/')
	elif request.method == 'GET':
		form = MatchingForm()
	else:
		form = MatchingForm()
	return render(request, 'matching/creatematching.html', {"form":form})
	
@login_required()
def complete(request):
	return render(request, 'matching/complete.html')

@login_required()	
def view_matching(request, title):
	#try:
		matching = Matching.objects.get(title = title)
		context = {'title': matching.title, 'left_one': matching.left_one, 'left_two': matching.left_two,
				   'left_three': matching.left_three, 'left_four': matching.left_four,
				   'right_one': matching.right_one, 'right_two': matching.right_two,
				   'right_three': matching.right_three, 'right_four': matching.right_four}
		return render(request, 'matching/answermatching.html', context)
	#except:
		return render(request, 'Video_page/404.html')