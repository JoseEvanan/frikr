"""Frikr URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from photos.views import home, detail, create
from users.views import login, logout
# r le dice que es una expresion regular  -^ iniciode cadena - $ fin de cadena
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Photo URLs
    url(r'^$', home, name="photos_home"),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name="photo_detail"),
    url(r'^photos/new/$', create, name="photo_create"),

    #Users URLs
    url(r'^login$', login, name='users_login'),
    url(r'^logout$', logout, name='users_logout')
]
#path('accounts/', include('accounts.urls')),