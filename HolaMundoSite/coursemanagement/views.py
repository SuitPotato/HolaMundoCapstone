# Django Imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import models

# Course Management App Imports
from coursemanagement.models import Lesson
from coursemanagement.models import Course
from coursemanagement.forms import LessonForm
from UserSettingsPage.models import Preference
from coursemanagement.models import CourseLessonQuiz, Course, Lesson, Quiz

# Import User
from django.contrib.auth.models import User


# Create your views here.


# Purpose of the manage is to show all the courses related to the same author
@login_required()
def manage(request):
	
	# Filters out courses only made by the user
	current_user = request.user
	courses = Course.objects.filter(author = current_user)
	lessons = Lesson.objects.filter(author = current_user)
	context = {"courses":courses, "lessons":lessons}
	return render(request, 'coursemanagement/manage.html', context)

# Purpose of viewcourse is to show the lessons specific course.
# Takes in a request and the courseID
# Need to verify if the author is the current user, if not redirect
@login_required()
def viewcourse(request, courseID):
	current_user = request.user
	# Retrieving one value, so no filter needed, but get instead
	# Follows the format (for looking up stuff):
		# field__lookuptype=value
		# courseID__exact = courseID
	course = Course.objects.get(courseID__exact = courseID)
	if(courses.author == current_user):
		
		context = {"course":course}
		return render(request, 'coursemanagement/viewcourse.html',context)
	else:
		# Just a temporary flag
		# Should return a 404
		return render(request, 'mainpage/DragDemo.html')

@login_required()
def success(request):
    return render(request, 'coursemanagement/success.html')

@login_required()
def lesson(request):
    if request.method == 'POST':
        # form is a variable that contains the courseform
        form = LessonForm(request.POST)
        if form.is_valid():
            # Instantiate the class Course from Models
            v = Lesson()
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
        form = LessonForm()
    else:
        form = LessonForm()
    return render(request, "coursemanagement/courseform.html", {"form": form})


def load_course(request, link, number):
        print('Link: ' + link + '.')
        print('number: ' + number + ".")
        course = Course.objects.get(link=link)
        print(course)
        allInCourse = CourseLessonQuiz.objects.filter(courseID=course).values()
        toDisplay = allInCourse[0]
        print(toDisplay)

        #if request.user.is_authenticated():
            #pref = Preference.objects.get(user=request.user)
            #pref.fourthLastVid = pref.thirdLastVid
            #pref.thirdLastVid = pref.secondLastVid
            #pref.secondLastVid = pref.lastVid

            #pref.save()

        #if toDisplay.QuizID:
            #sentence = toDisplay.QuizID
            #context = {'title': sentence.title, 'wordOne': sentence.wordOne, 'wordTwo': sentence.wordTwo,
                  #     'wordThree': sentence.wordThree, 'wordFour': sentence.wordFour,
             #          'wordFive': sentence.wordFive}
            #return render(request, 'DragAndDropQuiz/sentenceTwo.html', context)

        #else:
        video = Lesson.objects.get(lessonID=toDisplay["LessonID_id"])
        print(video)
        context = {'video': video.youtube, 'title': video.title, 'tab1': video.tab1, 'tab2': video.tab2,
                   'tab3': video.tab3, 'tab4': video.tab4, 'tab5': video.tab5, 'tab6': video.tab6,
                   'tab1desc': video.tab1desc, 'tab2desc': video.tab2desc, 'tab3desc': video.tab3desc,
                   'tab4desc': video.tab4desc, 'tab5desc': video.tab5desc, 'tab6desc': video.tab6desc}
        return render(request, 'Video_page/videoloader.html', context)

        return render(request, 'Video_page/404.html')