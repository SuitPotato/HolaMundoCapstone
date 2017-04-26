import random

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from mainpage.forms import *
from coursemanagement.models import Lesson
from UserSettingsPage.models import Preference

from forms import UserForm


# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')


def drag(request):
    return render(request, 'mainpage/sentenceTwo.html')


def results(request, tag='all'):
	
	# Should always be hit. Gets tag, which is the text the user searched for
    if request.method == 'GET':
        tag = request.GET.get('query')

	# If the user hit the search button without putting in a query
    if tag == '':
	
		# If the user searches without a query, we return all videos. If this functionality would be changed it is changed here
        videos = Lesson.objects.all()
        context = {"videos": videos}
        return render(request, 'mainpage/results.html', context)
	
	# If the user searched a specific query
    else:
	
		# This line takes all videos in the database, and if the video's tags contain any word in the query, we keep that video. If the video's difficulty
		# is in the query, we add those videos as well. If nothing in the user's query is in the tags or difficulty, the video is excluded.
		# If any of this functionality is to be changed, change it below
        videos = [video for video in Lesson.objects.all() if any(text.lower() in video.tags.lower() or text.lower() in video.difficulty.lower() for text in tag.split())]
        context = {"videos": videos}
        return render(request, 'mainpage/results.html', context)


def loginview(request):
    return render(request, 'mainpage/login.html')


def lexusadduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # Redirect, or however we want to return back to the main view

            # HttpResponse is based off of URL Response, not Views
            return HttpResponseRedirect('/loginview/')
    else:
        form = UserForm()
    return render(request, 'mainpage/adduser.html', {'form': form})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
	
        # Change from LoginView to the acutal Login Page later
        return HttpResponseRedirect('/loginview/')


def logout(request):
    logout(request)
	
    # Change from LoginView to the acutal Login Page later
    return HttpResponseRedirect('/loginview/')


def register(request):

	# If page is loaded and a user submits registration form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

			# Create user if data put in register form is valid
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            g = Group.objects.get(name=form.cleaned_data['groups'])
            g.user_set.add(user)
			
			# Create preferences for the new user, preferences are a separate table than users, and have user as a foreign key attribute
            pref = Preference.objects.create(user=user)
			
			# Log in the new registered user so they can immediately access the site as a logged in user
            auth_login(request, user)
            return HttpResponseRedirect('/registered/')
	
	# Load the page, with an empty form. This will then be filled out and passed to this same function, under 'POST'
    form = RegistrationForm()
    return render(request, 'mainpage/register.html', {'form': form})


# Successfully registered users get redirected here
def registered(request):
    return render(request, 'mainpage/registered.html')


# myHolaMundo page is a customized page, where users will view their last viewed video as well as other suggest videos
# Videos suggested now randomly, eventually by a score they get based on their performance
@login_required()
def myHolaMundo(request):
    user_preferences = Preference.objects.get(user=request.user)
	
    videos_by_author = Lesson.objects.filter(author=request.user).values()
	
	# Currently random videos uploaded by you, later will be changed to match variable name
    six_random_videos_by_author = random.sample(videos_by_author, 6) 
	
	# Currently random videos uploaded by you, later will be changed to match variable name
    six_random_videos_by_difficulty = random.sample(videos_by_author, 6)
	
	# Pass user preferences, 6 videos by author/difficulty to dashboard.html to populate video displays at the bottom of the page
    context = {'user': request.user, 'prefs': user_preferences, 'videos_author': six_random_videos_by_author, 'videos_difficulty': six_random_videos_by_difficulty}
    return render(request, 'mainpage/dashboard.html', context)
	
def denied(request):
	return render(request, 'mainpage/denied.html')
