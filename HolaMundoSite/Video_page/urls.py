from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^video/(?P<link>[\w]+)$', views.load_video, name='video_loader'),
    ]
