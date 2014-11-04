from django.conf.urls import patterns, url
from shika import views

urlpatterns = patterns('',
            url(r'^$', views.home, name='home'),
            url(r'collection/$', views.collection, name='collection'),
            url(r'bookentry/$', views.book_entry, name='bookentry'),
            url(r'thanks/$', views.thanks, name='thanks'),
            )

