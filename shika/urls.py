from django.conf.urls import patterns, url
from shika import views

urlpatterns = patterns('',
            url(r'^$', views.home, name='home'),
            url(r'collection/$', views.collection, name='collection'),
            url(r'allcollections/$', views.allcollections, name='allcollection'),
            url(r'bookentry/$', views.book_entry, name='bookentry'),
            url(r'lending/$', views.lending_request, name='lending'),
            url(r'records/$', views.lending_records, name='records'),
            url(r'confirm/$', views.confirm_request, name='confirm'),
            url(r'thanks/$', views.thanks, name='thanks'),
            )

