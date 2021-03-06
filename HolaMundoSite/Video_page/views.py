from django.shortcuts import render
from django.http import HttpResponse
from coursemanagement.models import Lesson
from UserSettingsPage.models import Preference
# from coursemanagement.forms import LessonForm

# Create your views here:
def load_video(request, link):
    try:
        video = Lesson.objects.get(link=link)
        # if request.method == 'POST':
        #     form = LessonForm(request.POST)
        #     if form.is_valid():
        #         l = Lesson()
        #         l.save()
        if request.user.is_authenticated():
            pref = Preference.objects.get(user=request.user)
            pref.fourthLastVid = pref.thirdLastVid
            pref.thirdLastVid = pref.secondLastVid
            pref.secondLastVid = pref.lastVid
            pref.lastVid = video
            pref.save()

        tabInfo = [(video.tab1, video.tab1desc), (video.tab2, video.tab2desc), (video.tab3, video.tab3desc),
                   (video.tab4, video.tab4desc), (video.tab5, video.tab5desc), (video.tab6, video.tab6desc)]
        cleanTabInfo = []
        for tab in tabInfo:
            if tab[0] == "" or tab[0] is None or tab[1] == "" or tab[1] is None:
                pass
            else:
                cleanTabInfo.append(tab)

        print(cleanTabInfo)
        context = {'video': video.youtube, 'title': video.title, 'tabInfo': cleanTabInfo}
        return render(request, 'Video_page/video.html', context)
    except:
        return render(request, 'Video_page/404.html')
