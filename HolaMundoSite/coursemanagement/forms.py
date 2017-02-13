# Django Imports
from django import forms
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import ModelForm

# Course Management Imports
from coursemanagement.models import Lesson

#class CourseForm(forms.Form):


class LessonForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off of the model
		model = Lesson
		fields = ['title', 'youtube', 'link', 'tabs', 'tab1desc', 'tab2desc', 
			'tab3desc', 'tab4desc', 'tab5desc', 'tab6desc']
			
	# Choices: NUM_TABS
	NUM_TABS = (
	('ONE', '1'),
	('TWO', '2'),
	('THREE','3'),
	('FOUR', '4'),
	('FIVE','5'),
	('SIX','6'),
	)
	
	# Fields
	title = forms.CharField(max_length = 140)
	youtube = forms.CharField(max_length = 100)
	link = forms.CharField(max_length = 15)
	tabs = forms.ChoiceField(choices = NUM_TABS)
	tab1desc = forms.CharField(max_length = 2000, strip = True)
	tab2desc = forms.CharField(max_length = 2000, strip = True)
	tab3desc = forms.CharField(max_length = 2000, strip = True)
	tab4desc = forms.CharField(max_length = 2000, strip = True)
	tab5desc = forms.CharField(max_length = 2000, strip = True)
	tab6desc = forms.CharField(max_length = 2000, strip = True)