from django.conf.urls import patterns, url
#from computadora.apps.armadopc import views
from computadora.apps.armadopc.views import *
urlpatterns = patterns('',
	
	url(r'^addplaca/$',addPlaca),
	url(r'^verplaca/page/(?P<pagina>.*)/$',placa,name='vista_placa'),
	url(r'^placa/(?P<id_placa>.*)/$',Splaca,name='vista_splaca'),
	url(r'^edit/placa/(?P<id_placa>.*)/$',EditPlaca,name='vista_edit_Placa'),
	url(r'^eliminar/(?P<id_placa>\d+)/$',eliminar_pla,name="eliminar_placa"),

	url(r'^addcomponente/$',SubirComponent,name="add_componente"),
	url(r'^componente/page/(?P<pagina>.*)/$',componente,name="vista_component"),
	url(r'^componentes/(?P<id_comp>.*)/$',Scomponent,name='vista_Ver_componente'),
	url(r'^edit/componentes/(?P<id_comp>.*)/$',EditComponente,name='vista_edit_compo'),
	url(r'^eliminar/comp/(?P<id_comp>\d+)/$',eliminar_comp,name="eliminar_componente"),
	
	
	url(r'^categoria/page/(?P<pagina>.*)/$',categoria,name="vista_categoria"),
	url(r'^addcategoria/$', addcategoria,name="add_categoria"),
	url(r'^eliminar/cat/(?P<id_c>\d+)/$',eliminar_cat,name="eliminar_categoria"),

	url(r'^principal1/$', principal1),
	url(r'^principal2/$', principal2),
	url(r'^principal3/$', principal3),

	#===============Armado PC===============

    url(r'^armar/$',armar),
    url(r'^crear/catalogo/$',crear_catalogo),
	url(r'^placa/$','computadora.apps.armadopc.views.lista_placa'),
	url(r'^componente/$','computadora.apps.armadopc.views.lista_componente'),
)