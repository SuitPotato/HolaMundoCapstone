"""SimpleSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from SimpleSite.views import home, about, register, userlogin, userlogout, get_lists, add_list, edit_list, remove_list, list_users, add_listuser, remove_user, list_items, create_item, add_item, remove_item, edit_item

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^about/', about, name='about'),

    url(r'^register/', register, name='register'),
    url(r'^login/',  userlogin, name='login'),
    url(r'^logout/', userlogout, name='logout'),

    url(r'^lists/', get_lists, name='lists'),
    url(r'^list_items/(?P<list_id>\w+)/$', list_items, name='list_items'),
    url(r'^list_users/(?P<list_id>\w+)/$', list_users, name='list_users'),

    url(r'add_list/$', add_list, name='add_list'),
    url(r'edit_list/(?P<list_id>\w+)/$', edit_list, name='edit_list'),
    url(r'remove_list/(?P<list_id>\w+)/$', remove_list, name='remove_list'),

    url(r'list/(?P<list_id>\w+)/add_user/$', add_listuser, name='add_listuser'),
    url(r'list/(?P<list_id>\w+)/remove_user/(?P<bridge_id>\w+)/$', remove_user, name='remove_user'),

    url(r'list_items/(?P<list_id>\w+)/create_item/$', create_item, name='create_item'),
    url(r'list_items/(?P<list_id>\w+)/add_item/$', add_item, name='add_item'),
    url(r'list_items/(?P<list_id>\w+)/edit_item/(?P<item_id>\w+)/$', edit_item, name='edit_item'),
    url(r'list_items/(?P<list_id>\w+)/remove_item/(?P<bridge_id>\w+)/$', remove_item, name='remove_item'),
    url(r'^', home, name='home'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
