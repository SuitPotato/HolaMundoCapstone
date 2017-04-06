"""Course Management URL Configuration

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

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manage/$', views.manage),
    url(r'^createlesson', views.lesson),
    url(r'^createcourse', views.course),
    url(r'^success', views.success),
    url(r'^viewcourse/(\d+)/', views.viewcourse),  # Takes in a CourseID, check coursemanagement/views.py for more
    url(r'^course/(?P<link>[\w]+)/(?P<number>[\w]+)$', views.load_course, name='course_loader'),
    url(r'^quizresults/(?P<q>[\w]+)/(?P<pk>[\w]+)$', views.quiz_results),
    url(r'^multiplechoice/$', views.create_multiple_choice_quiz),
    url(r'^multiplechoice/(?P<q>[\w]+)/(?P<d>[\w]+)$', views.create_multiple_choice_quiz_q),
    url(r'^multiplechoice/take/(?P<quiz>[\w]+)/', views.take_quiz)

    # url(r'^create', views.create),
    # url(r'^createcourse', views.course),
    # url(r'^createquize', views.quiz),

]
