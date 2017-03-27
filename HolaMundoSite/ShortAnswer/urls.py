
"""
HolaMundoSite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^ShortAnswer/$', views.create_essay_quiz, name='create_essay'),
    url(r'^ShortAnswer/(?P<quizID>[\w]+)/$', views.take_quiz, name='take_quiz'),
    url(r'^ShortAnswer/$', views.results, name='results'),
	#url(r'^ShortAnswer/(?P<title>[\w]+)$', views.view_essay_quiz, name='view_essay'),
    #url(r'^ShortAnswer/(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    
]