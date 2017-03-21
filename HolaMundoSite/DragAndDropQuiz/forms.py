# Django Imports
from django import forms
from django.db import models
from django.forms import ModelForm

# Import Model
from DragAndDropQuiz.models import DragAndDrop

# Form Classes
class DragAndDropForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off of the models
		model = DragAndDrop
		fields = []
		
	# Fields defined under forms.____