# Django Imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.db import models

# Course Management App Imports
from coursemanagement.models import Videos
from coursemanagement.forms import CourseForm


# Create your views here.

def manage(request):
    return render(request, 'coursemanagement/manage.html')


def success(request):
    return render(request, 'coursemanagement/success.html')


def course(request):
    if request.method == 'POST':
        # form is a variable that contains the courseform
        form = CourseForm(request.POST)
        if form.is_valid():
            # Instantiate the class Course from Models
            v = Videos()
            v.title = form.cleaned_data["title"]
            v.link = form.cleaned_data["link"]
            v.youtube = form.cleaned_data["youtube"]
            v.tabs = form.cleaned_data["tabs"]
            v.tab1desc = form.cleaned_data["tab1desc"]
            v.tab2desc = form.cleaned_data["tab2desc"]
            v.tab3desc = form.cleaned_data["tab3desc"]
            v.tab4desc = form.cleaned_data["tab4desc"]
            v.tab5desc = form.cleaned_data["tab5desc"]
            v.tab6desc = form.cleaned_data["tab6desc"]
            # Must save the instantiated variables afterwards
            v.save()

            # Make sure HttpResponseRedirect has a view and URL
            return HttpResponseRedirect('/success/')
    elif request.method == 'GET':
        form = CourseForm()
    else:
        form = CourseForm()
    return render(request, "coursemanagement/courseform.html", {"form": form})
