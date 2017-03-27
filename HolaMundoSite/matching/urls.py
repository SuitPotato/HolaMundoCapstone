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
	url(r'^get_number', views.get_number),
	url(r'^get_questions', views.get_questions),
	url(r'^answer_question', views.answer_question),
	url(r'^create_matching', views.create_matching),
	url(r'^complete', views.complete),
	url(r'^view_matching', views.view_matching),
]