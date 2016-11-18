from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^classes$', views.classes),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^no$', views.no),
    url(r'^yes/(?P<id>\d+)$', views.yes)
]
