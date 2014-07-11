#encoding:utf-8
from django.forms import ModelForm
from django.db import models
from django import forms
from models import *


class fcarrito(ModelForm):
    class Meta:
        model=Carrito
        exclude=['placa','id_sesion','estado']