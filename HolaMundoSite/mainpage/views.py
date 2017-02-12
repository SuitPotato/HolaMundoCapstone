from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from forms import UserForm

# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')

def drag(request):
	return render(request, 'mainpage/DragDemo.html')
	
def results(request):
	return render(request, 'mainpage/results.html')
	
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
	return render(request, 'mainpage/adduser.html', {'form':form})
	
def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
	else:
		# Change from LoginView to the acutal Login Page later
		return HttpResponseRedirect('/loginview/')

def logout(request):
	logout(request)
	# Change from LoginView to the acutal Login Page later
	return HttpResponseRedirect('/loginview/')