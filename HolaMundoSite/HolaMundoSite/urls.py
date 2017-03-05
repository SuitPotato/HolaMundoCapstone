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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainpage.urls')),
    url(r'^', include('UserSettingsPage.urls')),
    url(r'^', include('Video_page.urls')),
    url(r'^', include('coursemanagement.urls')),
    url(r'^', include('youtube.urls')),
<<<<<<< HEAD
	url(r'^matching', include('matching.urls', namespace="matching")),
	url(r'^TrueOrFalse', include('TrueOrFalse.urls', namespace="TrueOrFalse")),
=======
    url(r'^matching', include('matching.urls')),
    url(r'^', include('DragAndDropQuiz.urls')),
>>>>>>> refs/remotes/origin/master
]
