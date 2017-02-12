from django.shortcuts import render
from django.http import HttpResponse
from Video_page.models import Video


# Create your views here.

def index(request):
    return render(request, 'youtube/index.html')
