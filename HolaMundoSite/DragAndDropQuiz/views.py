from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import models
from django.shortcuts import render

# Course Management App Imports

from DragAndDropQuiz.models import Sentence
from DragAndDropQuiz.forms import SentenceForm

# Import User
from django.contrib.auth.models import User



# Create your views here.
def view_dragndrop(request):
    return None


def create_dragndrop(request):
    return None
	
	
# The following views are using the new method of Drag and drop
# Names can be changed later, current name is not as effective
def view_sentence_drag(request, title):
	try:
		sentence = Sentence.objects.get(title = title)
		context = {'title': sentence.title, 'wordOne': sentence.wordOne,'wordTwo': sentence.wordTwo,
					'wordThree': sentence.wordThree, 'wordFour': sentence.wordFour, 'wordFive': sentence.wordFive}
		return render(request, 'DragAndDropQuiz/sentence.html', context)
	except:
		return render(request, 'Video_page/404.html')

def view_sentence_dragTwo(request, title):
	try:
		sentence = Sentence.objects.get(title=title)
		context = {'title': sentence.title, 'wordOne': sentence.wordOne, 'wordTwo': sentence.wordTwo,
				   'wordThree': sentence.wordThree, 'wordFour': sentence.wordFour,
				   'wordFive': sentence.wordFive}
		return render(request, 'DragAndDropQuiz/sentenceTwo.html', context)
	except:
		return render(request, 'Video_page/404.html')

@login_required()
def create_sentence_drag(request):
	if request.method == 'POST':
		# Form is a variable that contains the source form
		form = SentenceForm(request.POST)
		if form.is_valid():
			# Specifically calling the model
			v = Sentence()
			v.title = form.cleaned_data["title"]
			v.wordOne = form.cleaned_data["wordOne"]
			v.wordTwo = form.cleaned_data["wordTwo"]
			v.wordThree = form.cleaned_data["wordThree"]
			v.wordFour = form.cleaned_data["wordFour"]
			v.wordFive = form.cleaned_data["wordFive"]
			# Must save the variables into the model
			v.save()
			
			# HttpResponseRedirect has a view and URL
			# Currently a flag, no success screen yet
			return HttpResponseRedirect('/success/')
	elif request.method == 'GET':
		form = SentenceForm()
	else:
		form = SentenceForm()
	return render(request, 'DragAndDropQuiz/sentence_create.html', {"form":form})
			
			
@login_required
def success(request):
	return render(request, 'DragAndDropQuiz/success.html')