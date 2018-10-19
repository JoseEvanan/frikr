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
from django.contrib.auth.decorators import login_required

from photos.views import (HomeView, DetailView, CreateView, PhotoListView,
                            UserPhotosView)
from users.views import LoginView, LogoutView
# r le dice que es una expresion regular  -^ iniciode cadena - $ fin de cadena
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Photo URLs
    url(r'^$', HomeView.as_view(), name="photos_home"),
    url(r'^photos/(?P<pk>[0-9]+)/$', DetailView.as_view(), name="photo_detail"),
    url(r'^photos/new/$', CreateView.as_view(), name="photo_create"),
    url(r'^photos/$', PhotoListView.as_view(), name="photos_list"),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name="user_photos"),
    #Users URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout')
]
#path('accounts/', include('accounts.urls')),
