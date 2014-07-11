from django.conf.urls import patterns, url
#from computadora.apps.armadopc import views
from views import *

urlpatterns = patterns('',
	url(r'^$',index, name='index'),
	#url(r'^(?P<categoria_id>\d+)/$',detail, name='detail'),
	url(r'^logeo/$',logeo),
	url(r'^cerrar$',cerrar),
)