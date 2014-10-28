from django.conf.urls import patterns, url
from shika import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            )

