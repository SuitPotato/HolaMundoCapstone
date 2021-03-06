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
    url(r'^results/$', views.results),
    url(r'^results/(?P<page>[\w]+)/(?P<tag>[\w]+)$', views.results_p, name="resultspage"),
    url(r'^results/(?P<page>[\w]+)$', views.results, name="results"),
    url(r'^login/$', auth_views.login, {'template_name': 'mainpage/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'mainpage/logout.html'}, name='logout'),
    url(r'^register/$', views.register),
    url(r'^registered/$', views.registered),
    url(r'^myHolaMundo/$', views.myHolaMundo),
    url(r'^denied/$', views.denied, name='denied'),
]
