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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.index),
	url(r'^DragDemo/$', views.drag),
	url(r'^results/$', views.results),
	url(r'^loginview/$', views.loginview),
	url(r'^adduser', views.lexusadduser),
	url(r'^results/(?P<tag>[\w]+)$', views.results, name="results"),
	url(r'^login/$', auth_views.login, {'template_name': 'mainpage/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'mainpage/logout.html'}, name='logout'),
<<<<<<< HEAD
    url(r'^fillintheblank/$', include('fillintheblank.urls')),

=======
	url(r'^register/$', views.register),
    url(r'^UserSettingsPage/', include('UserSettingsPage.urls')),
	url(r'^registered/$', views.registered)
>>>>>>> master
]
