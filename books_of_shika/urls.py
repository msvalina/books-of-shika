from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'books_of_shika.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'shika.views.index', name='shika'),
    url(r'^shika/', include('shika.urls', namespace="shika")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

)
