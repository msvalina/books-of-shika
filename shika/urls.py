from django.conf.urls import patterns, url
from shika import views

urlpatterns = patterns('',
            url(r'^$', views.home, name='home'),
            url(r'collection$', views.collection, name='collection'),
            )

