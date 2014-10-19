# coding:utf8

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from photowall.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'photowall.views.home', name='home'),
                       # url(r'^photowall/', include('photowall.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url('^$', my_homepage_view),
                       url(r'^cal/', include('photowall.linkcalendar.urls')),
                       )


# Serving static files in development
urlpatterns += staticfiles_urlpatterns()
