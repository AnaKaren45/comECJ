from django.shortcuts import render,render_to_response
# Create your views here.
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
# importando el paginador
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from computadora.apps.cliente.forms import *
from computadora.apps.armadopc.models import *

import json

import hashlib
import datetime
#=======================Para Reporte==============
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
#from computadora.apps.armadopc.models import *
import datetime


###############   Placa    ##################

def placa2(request,pagin):
	lista_placa =Placa.objects.all()
	paginator=Paginator(lista_placa,3)#cuantos productos quieres mostrar
	try:
		page = int(pagin)
	except:
		page = 1
	try:
		placa=paginator.page(page)
	except (EmptyPage,InvalidPage):
		placa=paginator.page(paginator.num_pages)
	return render_to_response("cliente/lista_placas.html",{"placa":placa},context_instance=RequestContext(request))

def verplaca(request,id_placa):
    placa=Placa.objects.get(id=id_placa)
    return render_to_response("cliente/verplaca.html",{"placa":placa},context_instance=RequestContext(request))
############## COMPONENTE #########################
def componente2(request,pagin):
	lista_form = Componente.objects.all()
	paginator=Paginator(lista_form,10)#cuantos productos quieres mostrar
	try:
		page = int(pagin)
	except:
		page = 1
	try:
		placa=paginator.page(page)
	except (EmptyPage,InvalidPage):
		placa=paginator.page(paginator.num_pages)
	return render_to_response("cliente/lista_componentes.html",{"componente":placa},context_instance=RequestContext(request))

def vercomponent(request,id_comp):
	comp=Componente.objects.get(id=id_comp)
	#cats=comp.categorias.all() #Obteniendo la categoria del componente
  
	return render_to_response("cliente/vercomponente.html",{"componente":comp},context_instance=RequestContext(request))
############para carrit placas#############3

def cargar_carrito(request,id):
    pro=Placa.objects.get(id=int(id))
    fcarr=fcarrito()
    return render_to_response("cliente/fcarrito.html",{'fcarr':fcarr,'pro':pro},context_instance=RequestContext(request))

def carrito_add1(request,id,cantidad):
    return HttpResponse("Hola"+cantidad)
    #if request.method=="POST":
    #    cant=request.POST['cantidad']
    #    if int(cantidad)>0:
    #        pro=Placa.objects.get(id=int(id))
    #        #carr=Carrito.objects.create(id_sesion=request.session["id_sesion"],estado=False,producto=pro,cantidad=int(cant))
    #        if not "contador" in request.session:
    #            request.session['contador'] = 0
    #        contador=request.session['contador']
    #        request.session['contador']=contador+1
    #return HttpResponse(request.session['contador'])
def carrito_add1(request,id,cantidad):
    ver=request.method
    if request.method=="GET":
        if int(cantidad)>0:
            pro=Componente.objects.get(id=int(id))
            carr=Carrito.objects.create(id_sesion="Ana - Caren",estado=False,placa=pro.id,cantidad=int(cantidad))
            if not "contador1" in request.session:
                request.session['contador1'] = 0
            contador=request.session['contador1']
            request.session['contador1']=contador+1
    return HttpResponse(request.session['contador1'])

def carrito_add(request,id,cantidad):
    ver=request.method
    if request.method=="GET":
        if int(cantidad)>0:
            pro=Placa.objects.get(id=int(id))
            carr=Carrito.objects.create(id_sesion="Ana Caren",estado=False,placa=pro.id,cantidad=int(cantidad))
            if not "contador" in request.session:
                request.session['contador'] = 0
            contador=request.session['contador']
            request.session['contador']=contador+1
    return HttpResponse(request.session['contador'])

def confirmar_compra(request):
    placa=Placa.objects.all()
    carr=Carrito.objects.filter(estado=0)
    return render_to_response("cliente/confirmar_compra.html",{'placa':placa,'carr':carr},context_instance=RequestContext(request))

def confirmar_compra1(request):
    compo=Componente.objects.all()
    carr=Carrito.objects.filter(estado=0)
    return render_to_response("cliente/confirmar_compra1.html",{'compo':compo,'carr':carr},context_instance=RequestContext(request))

   

def eliminar_carrito(request,id):
    if "contador" in request.session:
        contador=request.session['contador']
        request.session['contador']=contador-1
        carr=Carrito.objects.get(id=int(id))
        carr.delete()
        placa=Placa.objects.all()
        carr=Carrito.objects.filter(estado=0)
        return render_to_response("cliente/confirmar_compra.html",{'placa':placa,'carr':carr},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("")

def guardar_carrito(request):    
    carr=Carrito.objects.filter(estado=0)
    for i in carr:
        i.estado=1
        i.save()
    request.session['contador']=0
    placa=Placa.objects.all()
    carr=Carrito.objects.filter(estado=0)
    return render_to_response("cliente/confirmar_compra.html",{'placa':placa,'carr':carr},context_instance=RequestContext(request))

def eliminar_carrito1(request,id):
    if "contador1" in request.session:
        contador=request.session['contador1']
        request.session['contador1']=contador-1
        carr=Carrito.objects.get(id=int(id))
        carr.delete()
        compo=Componente.objects.all()
        carr=Carrito.objects.filter(estado=0)
        return render_to_response("cliente/confirmar_compra1.html",{'compo':compo,'carr':carr},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("")

def guardar_carrito1(request):    
    carr=Carrito.objects.filter(estado=0)
    for i in carr:
        i.estado=1
        i.save()
    request.session['contador1']=0
    compo=Componente.objects.all()
    carr=Carrito.objects.filter(estado=0)
    return render_to_response("cliente/confirmar_compra1.html",{'compo':compo,'carr':carr},context_instance=RequestContext(request))


def carrito_mostrar(request):
    if not "contador" in request.session:
        request.session['contador'] = 0
    return HttpResponse(request.session['contador'])

#################para el carrito componente#############
def cargar_carrito1(request,id):
    pro=Componente.objects.get(id=int(id))
    fcarr=fcarrito()
    return render_to_response("cliente/fcarrito1.html",{'fcarr':fcarr,'pro':pro},context_instance=RequestContext(request))

#################Reporte###########
def inicio(request):
    return render_to_response("inicio.html",{},context_instance=RequestContext(request))

def reservas_dia(request):
    placa=Placa.objects.all()
    return render_to_response("reportes/reservas.html",{'reservas':placa},context_instance=RequestContext(request))

def crear_reporte(request):
    placa=Placa.objects.all()
    html=render_to_string("reportes/reportes.html",{'pagesize':'A4','venta':placa},context_instance=RequestContext(request))
    return generar_pdf(html)
def generar_pdf(html):
    resultado=StringIO.StringIO()
    pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
    return HttpResponse("Error en generar el pdf")
def ventas(request):
    placa=Placa.objects.all()
    compo=Componente.objects.all()
    carr=Carrito.objects.filter(estado=1)
    return render_to_response("reportes/ventas.html",{'compo':compo,'placa':placa,'carr':carr},context_instance=RequestContext(request))