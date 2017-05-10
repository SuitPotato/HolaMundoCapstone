import random

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def results(request, tag='', page=1):
    print(tag)
    if request.method == 'GET':
        tag = request.GET.get('tag', '')

    # If the user hit the search button without putting in a query
    if tag == '':
    
        # If the user searches without a query, we return all videos.
        # If this functionality would be changed it is changed here
        video_list = Lesson.objects.all()
        # if request is GET set page to 1

        # paginate video_list to 5 per page
        paginator = Paginator(video_list, 5)

        # paginate page
        try:
            videos = paginator.page(page)

        #  if user enters a letter and not an Integer, take them to page 1
        except PageNotAnInteger:
            videos = paginator.page(5)

        # if the user enters a page out of range, take to last page
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)
            
        context = {"videos": videos, "tag": tag, "page": page}
        return render(request, 'mainpage/results.html', context)
    
    # If the user searched a specific query
    else:
    
        # This line takes all videos in the database, and if the video's tags contain any word in the query, we keep
        # that video. If the video's difficulty
        # is in the query, we add those videos as well. If nothing in the user's query is in the tags or difficulty,
        #  the video is excluded.
        # If any of this functionality is to be changed, change it below
        video_list = [video for video in Lesson.objects.all() if any(text.lower()
                      in video.tags.lower() or text.lower() in video.difficulty.lower() for text in tag.split())]
        # if request is GET set page to 1
        page = request.GET.get('page', 1)

        # paginate video_list to 5 per page
        paginator = Paginator(video_list, 2)

        # paginate page
        try:
            videos = paginator.page(page)

        #  if user enters a letter and not an Integer, take them to page 1
        except PageNotAnInteger:
            videos = paginator.page(1)

        # if the user enters a page out of range, take to last page
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)

        context = {"videos": videos, 'tag': tag, 'page': page}
        return render(request, 'mainpage/results.html', context)


# Results function to handle other pages. Need both just incase a page, or tag, isn't specified.
def results_p(request, page=1, tag=''):
    video_list = [video for video in Lesson.objects.all() if any(
        text.lower() in video.tags.lower() or text.lower() in video.difficulty.lower() for text in tag.split())]

    paginator = Paginator(video_list, 2)
    try:
        videos = paginator.page(page)

    except PageNotAnInteger:
        videos = paginator.page(1)

    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    context = {"videos": videos, 'page': page, 'tag': tag}
    return render(request, 'mainpage/results.html', context)


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
            
            #gets chosen group that user selected in choicefield (drop down menu)
            g = Group.objects.get(name=form.cleaned_data['groups'])
            
            #adds user to selected group in database
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


# function that renders template that lets user know that they do not have permission to access
# the current view (url) they are trying to access
def denied(request):
    return render(request, 'mainpage/denied.html')
