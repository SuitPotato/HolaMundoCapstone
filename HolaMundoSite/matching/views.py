from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import *

@login_required()
def get_number(request):
	if request.method == 'POST':
		form = MatchingNumber(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('question.html')
	else:
		form = MatchingNumber()
		return render(request, 'number.html', {'form': form})

@login_required()		
def get_questions(request):
	if request.method == 'POST':
		form = MatchingQuestion(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/completion/')
	else:
		form = MatchingQuestion()
		return render(request, 'question.html', {'form': form})

@login_required()		
def answer_question(request):
	if request.method == 'POST':
		form = MatchingQuestion(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/completion/')
	else:
		form = MatchingQuestion()
		return render(request, 'question.html', {'form': form})