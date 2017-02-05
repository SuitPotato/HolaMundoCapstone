from django import forms
from django.forms import ModelForm
from coursemanagement.models import  CourseForm

#class CourseForm(forms.Form):


class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = [title, youtube, link, tabs, tab1desc, tab2desc, 
			tab3desc, tab4desc, tab5desc, tab6desc]