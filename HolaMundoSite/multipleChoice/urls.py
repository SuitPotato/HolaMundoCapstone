"""HolaMundoSite URL Configuration
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

urlpatterns = [
    url(r'^multipleChoice/$', views.quiz),
    url(r'^multipleChoice/$', views.quiz, name='quiz'),
    url(r'^multipleChoice/submit/$', views.submit, name='submit'),
    # url(r'^takeQuiz/$', views.takeQuiz, name = 'takeQuiz')
    url(r'^multipleChoice/(?P<quizID>[\w]+)/$', views.view_takeQuiz, name='view_takeQuiz'),
    # url(r'^score/(?P<quizID>[\w]+)/$', views.score, name='score'),
    # url(r'^results/$', views.results, name = 'results'),
    # url(r'^(?P<quizID>[0-9]+)/results/$', views.results, name='results')
    # url(r'^multipleChoice/', 'multipleChoice.views.quiz', name = 'quiz'),
]
