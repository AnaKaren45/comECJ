from django.conf.urls import patterns, include, url
from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'armadopc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', inicio),
    url(r'^inicio1/$', inicio1),
    url(r'^logeo/$', logeo),
    url(r'^inicio2/$',inicio2),


	
)
