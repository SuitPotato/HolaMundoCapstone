from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from matching.forms import *

#This funciton asks user for the name of their quiz and the nuber of
#choices in their matching question

#login required refers to a user having to be logged in to be able to
#access the following content on all functions in the views file
#where it is located
@login_required()
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
			return HttpResponseRedirect('matching/question.html')
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
	return render(request, 'matching/answer.html', {'form': form})