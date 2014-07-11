from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader
from django.http import Http404
from django.template import RequestContext

# importando el paginador
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import PlacaForm,ComponentForm,CategoriaForm
from computadora.apps.armadopc.models import *
import json

#=============PROFORMA===============
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from computadora.apps.armadopc.models import *
import datetime
# <img {{imagen.path }}>

def crear_catalogo(request):
    if request.method=='POST':
    	id_placa=request.POST["splaca"]
    	cat_num=Categoria.objects.all()
    	procesador=request.POST['categoria1']
    	targeta_video=request.POST['categoria2']
    	targeta_sonido=request.POST['categoria3']
    	memoria_ram=request.POST['categoria4']
    	#return HttpResponse(targeta_sonido)
    	placa=Placa.objects.get(id=int(id_placa))
    	compo_pro=Componente.objects.get(id=int(procesador))
    	compo_video=Componente.objects.get(id=int(targeta_video))
    	compo_sonido=Componente.objects.get(id=int(targeta_sonido))
    	memoria_ram=Componente.objects.get(id=int(memoria_ram))
    	total=placa.precio+compo_pro.precio+compo_sonido.precio+compo_video.precio+memoria_ram.precio
        html=render_to_string("reportes/reportes.html",{'pagesize':'A4','placa':placa,'compo_pro':compo_pro,'compo_video':compo_video,'compo_sonido':compo_sonido,'memoria_ram':memoria_ram,'total':total},context_instance=RequestContext(request))
    	return generar_pdf(html)
#REPORTE


def generar_pdf(html):
    resultado=StringIO.StringIO()
    pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
    return HttpResponse("Error en generar el pdf")
#REPORTE
def armar(request):
    if request.method=='POST':
        pla=request.POST['splaca']
        placa1=Placa.objects.get(id=int(pla))
        catego=Categoria.objects.all()
        compo=Componente.objects.filter(Categoria=catego,placa=placa1)
        return render_to_response("placas/formulario.html",{"compo":compo,'catego':catego},context_instance=RequestContext(request))
    placa=Placa.objects.all()
    cate=Categoria.objects.all()
    return render_to_response("placas/armar.html",{"placa":placa,'cate':cate},context_instance=RequestContext(request))
#===========PLANTILLAS===========
def principal1(request):
	return render_to_response("base/base1.html",context_instance=RequestContext(request))
def principal2(request):
	return render_to_response("base/base2.html",context_instance=RequestContext(request))
def principal3(request):
	return render_to_response("base/base3.html",context_instance=RequestContext(request))
#****placa******************************************************
def addPlaca(request):
	info_enviado= False
	if request.method=="POST":
		formulario=PlacaForm(request.POST,request.FILES)
		if formulario.is_valid():
		
			nombre = formulario.cleaned_data['nombre']
			imagen=formulario.cleaned_data['imagen']
			marca = formulario.cleaned_data['marca']
			zocalo = formulario.cleaned_data['zocalo'] 
			cant_BancosMemoria = formulario.cleaned_data['cant_BancosMemoria']
			cant_RanurasPci = formulario.cleaned_data['cant_RanurasPci']
			precio = formulario.cleaned_data['precio']
			p=Placa()
			if imagen:#validacion de imagen
				p.imagen = imagen
			p.nombre=nombre
			p.marca=marca
			p.zocalo=zocalo
			p.cant_BancosMemoria=cant_BancosMemoria
			p.cant_RanurasPci=cant_RanurasPci
			p.precio=precio
			p.save()
			info="se guardo satisfactoriamente"
		else:
			info="datos incorrectos"
		formulario=PlacaForm()
		ctx={'formulario':formulario,'informacion':info}
		return render_to_response("placas/addplaca.html",ctx,context_instance=RequestContext(request))
	else:	
		formulario=PlacaForm()
		ctx={'formulario':formulario}
	return render_to_response("placas/addplaca.html",ctx,context_instance=RequestContext(request))
		
def placa(request,pagina):
	
	lista_placa =Placa.objects.all()
	paginator=Paginator(lista_placa,3)#cuantos productos quieres mostrar
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		placa=paginator.page(page)
	except (EmptyPage,InvalidPage):
		placa=paginator.page(paginator.num_pages)

	return render_to_response("placas/placas.html",{"placa":placa},context_instance=RequestContext(request))
def Splaca(request,id_placa):
	placa=Placa.objects.get(id=id_placa)
	return render_to_response("placas/splaca.html",{"placa":placa},context_instance=RequestContext(request))

def EditPlaca(request,id_placa):
	p=Placa.objects.get(id=id_placa)
	# guardando de editplaca
	if request.method=="POST":
		form=PlacaForm(request.POST,request.FILES)
		if form.is_valid():
			nombre=form.cleaned_data['nombre']
			imagen=form.cleaned_data['imagen']
			marca=form.cleaned_data['marca']
			zocalo=form.cleaned_data['zocalo']
			cant_BancosMemoria = form.cleaned_data['cant_BancosMemoria']
			cant_RanurasPci = form.cleaned_data['cant_RanurasPci']
			precio=form.cleaned_data['precio']
			p.nombre=nombre
			p.marca=marca
			p.zocalo=zocalo
			p.cant_BancosMemoria = cant_BancosMemoria
			p.cant_RanurasPci=cant_RanurasPci
			p.precio=precio
			if imagen:   # verificamos q la imagen sea correcta
					p.imagen=imagen
			p.save()  #guardadndo el modelo de manera editar
			return HttpResponseRedirect('/placa/%s'%p.id)
	# recuperando el formulario 
	if request.method=="GET":
		form = PlacaForm(initial={
			'nombre':p.nombre,
			'marca':p.marca,
			'zocalo':p.zocalo,
			'cant_BancosMemoria':p.cant_BancosMemoria,
			'cant_RanurasPci':p.cant_RanurasPci,
			'precio':p.precio,
	
			})
	
	return render_to_response("placas/editarplaca.html",{'formulario':form,'componente':p},context_instance=RequestContext(request))	
def eliminar_pla(request,id_placa):
	placa=get_object_or_404(Placa,pk=id_placa).delete()
	return render_to_response("placas/eliminar.html",RequestContext(request))

#*****categoria***********************************************************************
def categoria(request,pagina):
	
	lista_categoria =Categoria.objects.all()
	paginator=Paginator(lista_categoria,3)
	try:
		page=int(pagina)
	except:
		page= 1
	try:
		categoria=paginator.page(page)
	except (EmptyPage,InvalidPage):
		categoria=paginator.page(paginator.num_pages)
	return render_to_response("categoria/categorias.html",{"categoria":categoria},context_instance=RequestContext(request))
def addcategoria(request):
	info_enviado= False
	nombre=""
	if request.method=="POST":
		formulario=CategoriaForm(request.POST)
		if formulario.is_valid():
			nombre=formulario.cleaned_data['nombre']
			c=Categoria()
			c.nombre=nombre
			c.status= True# que sea true a todos los objetos q llamemos
			c.save()# guardar la informacion
			info= "se guardo satisfactoriamente"
		else:
			info= "datos incorrectos"
		formulario =CategoriaForm()
		ctx={'formulario':formulario,'informacion':info}#contexto
		return render_to_response("categoria/addcategoria.html",ctx,context_instance=RequestContext(request))
	else:
		formulario=CategoriaForm()
		ctx={'formulario':formulario}
	return render_to_response("categoria/addcategoria.html",ctx,context_instance=RequestContext(request))
def eliminar_cat(request,id_c):
	categoria=get_object_or_404(Categoria,pk=id_c).delete()
	return render_to_response("categoria/eliminar.html",RequestContext(request))


#****componente***********************************************************************
def componente(request,pagina):
	
	lista_form = Componente.objects.all()
	paginator=Paginator(lista_form,3)#cuantos productos quieres mostrar
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		form=paginator.page(page)
	except (EmptyPage,InvalidPage):
		form=paginator.page(paginator.num_pages)
	return render_to_response("componente/componente.html",{"componente":form},context_instance=RequestContext(request))


def SubirComponent(request):
	info = "iniciado"
	if request.method == "POST":
		form= ComponentForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()#guardando la informacion
			form.save_m2m()#guarda la relacion ManyToMany
			info = "guardando satisfactoriamente"
			return HttpResponseRedirect('/componentes/%s'%add.id)
	else:
		form = ComponentForm()
	ctx ={'formulario':form,'informacion':info}
	return render_to_response("componente/addcomponent.html",ctx,context_instance=RequestContext(request))

def Scomponent(request,id_comp):
	comp=Componente.objects.get(id=id_comp)
	#cats=comp.categorias.all() #Obteniendo la categoria del componente
	ctx={"componente":comp}
	return render_to_response("componente/scomponente.html",ctx,context_instance=RequestContext(request))

def EditComponente(request,id_comp):
	info = "iniciado"
	comp = Componente.objects.get(id=id_comp)
	if request.method == "POST":
		form = ComponentForm(request.POST,request.FILES,instance=comp)
		if form.is_valid():
			edit_comp = form.save(commit=False)
			form.save_m2m()
			edit_comp.status = True
			edit_comp.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/componentes/%s/'%edit_comp.id)
	else:
		form = ComponentForm(instance=comp)
	ctx = {'formulario':form,'informacion':info}
	return render_to_response('componente/editcompo.html',ctx,context_instance=RequestContext(request))
def eliminar_comp(request,id_comp):
	dato=get_object_or_404(Componente,pk=id_comp).delete()	
	return render_to_response("componente/eliminar_comp.html",RequestContext(request))

def compatibilidad(request,id_placa):
	placa=Placa.objects.all()
	com=Componente.objects.all()
	for item in com:
		if idPlaca == id_placa:
			lista=com
		return render_to_response('compatibilidad.html',{'placa':placa,'com':com},context_instance=RequestContext(request))


def detalle(request):
	return render_to_response('detalles.html.html',context_instance=RequestContext(request))

def lista_placa(request):
    placa = placa.objects.filter(estado=True)
    return render_to_response('lista_placa.html', {'lista': placa}, context_instance=RequestContext(request))

def lista_componente(request):
    componente = componente.objects.filter(estado=True)
    return render_to_response('lista_componente.html', {'lista': componente}, context_instance=RequestContext(request))

