from django.conf.urls import patterns, url
#from computadora.apps.armadopc import views
from computadora.apps.cliente.views import *
urlpatterns = patterns('',
	
	
	url(r'^base/page/(?P<pagin>.*)/$',placa2),	
	url(r'^placas/(?P<id_placa>.*)/$',verplaca),
	url(r'^compo/page/(?P<pagin>.*)/$',componente2),
	url(r'^ventas/$',ventas),
	url(r'^vercomponente/(?P<id_comp>.*)/$',vercomponent),
	#para carrito placa####
	url(r'^cliente/cargar/carrito/(\d+)/$',cargar_carrito),
	url(r'^cliente/carrito/add/(\d+)/(\d+)/$',carrito_add),
	url(r'^cliente/carrito/add1/(\d+)/(\d+)/$',carrito_add1),
	url(r'^eliminar/carrito/(\d+)/$',eliminar_carrito),
	url(r'^guardar/carrito/$',guardar_carrito),
	url(r'^eliminar/carrito1/(\d+)/$',eliminar_carrito1),
	url(r'^guardar/carrito1/$',guardar_carrito1),
	url(r'^cliente/mostrar/carrito/$',carrito_mostrar),
	url(r'^confirmar/compra/$',confirmar_compra),
	url(r'^confirmar/compra1/$',confirmar_compra1),

	#para carrito componenrte
	url(r'^cliente/cargar/carrito1/(?P<id>.*)/$',cargar_carrito1),	

#============Reporte============
 	url(r'^$',inicio),
    url(r'^reserva/$',reservas_dia),
    url(r'^crear/reporte/$',crear_reporte),
)	
    
   
    
    




