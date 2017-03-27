from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from mainpage.forms import *
from coursemanagement.models import Lesson
from UserSettingsPage.models import Preference

from forms import UserForm


# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')


def drag(request):
    return render(request, 'mainpage/DragDemo.html')


def results(request, tag='all'):
    if request.method == 'GET':
        tag = request.GET.get('query', None)
        print(tag)

    if tag == '':
        videos = Lesson.objects.all()
        context = {"videos": videos}
        return render(request, 'mainpage/results.html', context)
    else:
        videos = [video for video in Lesson.objects.all() if any(text.lower() in video.tab2desc.lower() for text in tag.split())]
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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            pref = Preference.objects.create(user=user)
            auth_login(request, user)
            return HttpResponseRedirect('/registered/')
    form = RegistrationForm()
    return render(request, 'mainpage/register.html', {'form': form})


def registered(request):
    return render(request, 'mainpage/registered.html')


@login_required()
def myHolaMundo(request):
    prefs = Preference.objects.get(user=request.user)
    videos = Lesson.objects.filter(author=request.user).values()
    context = {'user': request.user, 'prefs': prefs, 'videos': videos}
    return render(request, 'mainpage/dashboard.html', context)
