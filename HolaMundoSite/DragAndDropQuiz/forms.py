# Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm

# Import Model
from DragAndDropQuiz.models import DragAndDrop
from coursemanagement.models import Quiz

# Form Classes
class DragAndDropForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off of the models
		model = DragAndDrop
		fields = ['title','content','wordOne','wordTwo','wordThree','wordFour','wordFive']
		
	# Fields defined under forms.____
	title = forms.CharField(max_length = 140)
	content = forms.CharField(max_length = 1000)
	
	# Extend later to accept more words
	wordOne = forms.CharField(max_length = 15)
	wordTwo = forms.CharField(max_length = 15)
	wordThree = forms.CharField(max_length = 15)
	wordFour = forms.CharField(max_length = 15)
	wordFive = forms.CharField(max_length = 15)
	
class SentenceForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off of the model
		model = Quiz
		fields = ['title','wordOne','wordTwo','wordThree','wordFour','wordFive']
		
	# Fields defined under forms.++++
	title = forms.CharField(max_length = 140)
	
	# Extend later to accept more words
	wordOne = forms.CharField(max_length = 15)
	wordTwo = forms.CharField(max_length = 15)
	wordThree = forms.CharField(max_length = 15)
	wordFour = forms.CharField(max_length = 15)
	wordFive = forms.CharField(max_length = 15)
	