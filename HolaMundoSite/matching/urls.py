from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^get_number', views.get_number),
	url(r'^get_questions', views.get_questions),
	url(r'^answer_question', views.answer_question),
]