from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')
	
def login(request):
	return render(request, 'mainpage/login.html')

def drag(request):
	return render(request, 'mainpage/DragDemo.html')