# Django Imports
from django import forms
from django.db import models
from django.http import HttpResponseRedirect
from django.forms import ModelForm

# Course Management Imports
from coursemanagement.models import Course
from coursemanagement.models import Lesson


class CourseForm(forms.Form):
	# Meta Class
	class Meta:
		# Based off of the model
		model = Course
		fields = ['title','description','difficulty'
		]

	# Difficulty Choices
	DIFFICULTIES = (
	('1', 'Beginner'),
	('2', 'Intermediate'),
	('3', 'Advanced'),
	)

	# Fields
	title = forms.CharField(max_length = 55)
	description = forms.CharField(widget=forms.Textarea, max_length = 300)
	difficulty = forms.ChoiceField(choices = DIFFICULTIES)


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
	title = forms.CharField(max_length = 55)
	youtube = forms.CharField(max_length = 100)
	link = forms.CharField(max_length = 15)
	tabs = forms.ChoiceField(choices = NUM_TABS)
	tab1desc = forms.CharField(max_length = 2000, strip = True)
	tab2desc = forms.CharField(max_length = 2000, strip = True)
	tab3desc = forms.CharField(max_length = 2000, strip = True)
	tab4desc = forms.CharField(max_length = 2000, strip = True)
	tab5desc = forms.CharField(max_length = 2000, strip = True)
	tab6desc = forms.CharField(max_length = 2000, strip = True)
