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
import coursemanagement.views
import youtube.views

urlpatterns = [

	# Basic Manage Stuff
    url(r'^manage/$', coursemanagement.views.manage),
	url(r'^manage/(?P<filter_results>[\w]+)/$', coursemanagement.views.manage),
	url(r'^manage/course/(?P<courseID>[\w]+)/$', coursemanagement.views.viewcourse),
    url(r'^manage/create/course', coursemanagement.views.course),
	url(r'^manage/create/lesson/(?P<courseID>[\w]+)$', youtube.views.indexlink),
	#url(r'^manage/create/quiz/)
	
	
	url(r'^manage/create/quiz/(?P<courseID>[\w]+)$', coursemanagement.views.create_quiz),
	#url(r'^manage/create/quiz/)
#    url(r'^createlesson', coursemanagement.views.lesson),

	
	# General 
    url(r'^success', coursemanagement.views.success),
    url(r'^viewcourse/(\d+)/', coursemanagement.views.viewcourse),  # Takes in a CourseID, check coursemanagement/views.py for more
    url(r'^course/(?P<link>[\w]+)/(?P<number>[\w]+)$', coursemanagement.views.load_course, name='course_loader'),
    url(r'^quizresults/(?P<q>[\w]+)/(?P<pk>[\w]+)$', coursemanagement.views.quiz_results),
	
	# Multiple Choice URL's
	
    url(r'^multiplechoice/$', coursemanagement.views.create_multiple_choice_quiz),
    url(r'^multiplechoice/(?P<q>[\w]+)/(?P<d>[\w]+)$', coursemanagement.views.create_multiple_choice_quiz_q),
    url(r'^multiplechoice/take/(?P<quiz>[\w]+)/', coursemanagement.views.take_quiz),
	
	# Multiple Choice in Courses
	url(r'^multiplechoice/(?P<courseID>[\w])$', coursemanagement.views.create_multiple_choice_quiz),
	url(r'^multiplechoice/(?P<q>[\w]+)/(?P<d>[\w]+)/(?P<courseID>[\w])$', coursemanagement.views.create_multiple_choice_quiz_q),

	
	# Matching URL's
	
	url(r'^matching/$', coursemanagement.views.create_matching_selection),
	url(r'^matching/(?P<difficulty>[\w]+)/(?P<options>[\w]+)/', coursemanagement.views.create_matching_quiz),
	
	# Short Answer URL's
	
	url(r'^shortanswer/$', coursemanagement.views.create_short_answer),
	url(r'^shortanswer/(\d+)/', coursemanagement.views.take_short_answer),
	
	# Drag and Drop URL's
	
	url(r'^draganddrop/$', coursemanagement.views.create_sentence_drag_and_drop),
	url(r'^draganddrop/(?P<words>[\w]+)/(?P<difficulty>[\w]+)/$', coursemanagement.views.create_sentence_drag_and_drop_two),
	url(r'^draganddrop/take/(?P<quiz>[\w]+)/$', coursemanagement.views.take_drag_and_drop),
	url(r'^dnd/take/(?P<quiz>[\w]+)/$', coursemanagement.views.take_drag_and_drop),
    # url(r'^create', views.create),
    # url(r'^createcourse', views.course),
    # url(r'^createquize', views.quiz),

]
