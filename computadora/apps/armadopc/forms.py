from django import forms
from django.forms import ModelForm
from models import Componente
from models import Categoria,Placa


class CategoriaForm(forms.Form):
	nombre= forms.CharField(max_length=60,widget=forms.TextInput())

class ComponentForm(forms.ModelForm):
	class Meta:
		model = Componente	


class PlacaForm(ModelForm):
    class Meta:
        model=Placa
		
		
