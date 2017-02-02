from django.shortcuts import render
from django.http import HttpResponse
from Video_page.models import Video

# Create your views here.

def index(request):
    return render(request, 'Video_page/videoloader.html')

def load_video(request, link):
	try:
		video = Video.objects.get(link=link)
		context = {'video' : video.youtube}
		return render(request, 'Video_page/videoloader.html', context)
	except:
		return render(request, 'Video_page/404.html')