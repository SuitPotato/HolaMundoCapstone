
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
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),
    url(r'^passwordform/$', views.passwordform, name="passwordform"),
    url(r'^UserSettingsPage', views.settings)
]