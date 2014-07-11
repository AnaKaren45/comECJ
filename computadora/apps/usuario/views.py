
from django.shortcuts import render,render_to_response
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader
from django.template import RequestContext

def index(request):
	return render_to_response("index.html",context_instance=RequestContext(request))
def logeo(request):
	#mensaje = ""
	#if request.user.is_authenticated():
		#return HttpResponseRedirect('/')
	#else:
		if request.method=="POST":
			form=AuthenticationForm(request.POST)
			if form.is_valid:
				username=request.POST["username"]
				password=request.POST["password"]
				user=authenticate(username=username,password=password)
				if user is not None:
					if user.is_active:
						login(request,user)
						return HttpResponseRedirect("/principal1")
					else:
						info = "no activo"
						return render_to_response("logeo.html",{"informacion":info},context_instance=RequestContext(request))
				else:
					info = "nombre y/o password incorrectos !!!!"	

				return render_to_response("base/logeo.html",{"form":form,"informacion":info},context_instance=RequestContext(request))
				
		else:
			form=AuthenticationForm()# retorna un formulario limpio
			return render_to_response("base/logeo.html",{"form":form},context_instance=RequestContext(request))
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')