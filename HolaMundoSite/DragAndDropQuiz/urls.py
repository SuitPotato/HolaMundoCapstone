
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

	# NEEDED URLS
	# 1. Creating Drag and Drop
	# 2. Viewing Drag and Drop
	# 3. Later editting drag and drop
	
urlpatterns = [
	url(r'^dragndrop/$', views.view_dragndrop, name='view_dnd'),
	url(r'^dragndrop/create/$', views.create_dragndrop, name='create_dnd'),
	url(r'^sentence/$', views.view_sentence_drag, name = 'view_sentence'),
	url(r'^createsentence/$', views.create_sentence_drag, name = 'create_sentence'),
]
