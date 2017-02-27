from django.shortcuts import render
from django.http import HttpResponse
from coursemanagement.models import Lesson


# Create your views here.


def index(request):
    return render(request, 'Video_page/videoloader.html')


def load_video(request, link):
    try:
        video = Lesson.objects.get(link=link)
        context = {'video': video.youtube, 'title': video.title, 'tab1': video.tab1, 'tab2': video.tab2,
                   'tab3': video.tab3, 'tab4': video.tab4, 'tab5': video.tab5, 'tab6': video.tab6, 
				   'tab1desc': video.tab1desc, 'tab2desc': video.tab2desc, 'tab3desc': video.tab3desc,
				   'tab4desc': video.tab4desc, 'tab5desc': video.tab5desc, 'tab6desc': video.tab6desc}
        return render(request, 'Video_page/videoloader.html', context)
    except:
        return render(request, 'Video_page/404.html')
