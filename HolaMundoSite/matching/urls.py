from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^getnumber/$', views.get_number, name='get_number'),
	url(r'^getquestions/$', views.get_questions, name='get_questions'),
]