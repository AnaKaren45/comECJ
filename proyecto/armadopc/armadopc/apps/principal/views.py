from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
import pdb


# Create your views here.
def logeo(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid):
			password=request.POST["password"]
			
			username=request.POST["username"]
			user=authenticate(username=username,password=password)
			if user:
				login(request,user)
				return HttpResponseRedirect("/inicio_admin")
			else:
				return render_to_response("nousuario.html",context_instance=RequestContext(request))
	else:
		form=AuthenticationForm()
	return render_to_response("logeo.html",{"form":form},context_instance=RequestContext(request))
def inicio1(request):
	return render_to_response("index.html",context_instance=RequestContext(request))
def inicio2(request):
	return render_to_response("index1.html",context_instance=RequestContext(request))
def inicio(request):
	return render_to_response("base.html",{},RequestContext(request))
