from django.shortcuts import render
from django.http import HttpResponse
from Video_page.models import Video

# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')
	
def login(request):
	return render(request, 'mainpage/login.html')

def drag(request):
	return render(request, 'mainpage/DragDemo.html')
	
def results(request):
	try:
		context = dict()
		context['videos'] = Video.objects.all()
		print(context)
		return render(request, 'mainpage/results.html', context)
	except:
		return render(request, 'Video_page/404.html')