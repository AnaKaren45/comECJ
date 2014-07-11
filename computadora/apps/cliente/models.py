from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from computadora.apps.cliente.models import *
#from venta.apps.usuarios.models import *
# Create your models here.
class Placa(models.Model):

	def url(self,filename):
		ruta="MultimediaData/Placa/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre  =models.CharField(max_length=20)
	imagen  =models.ImageField(upload_to=url,null=True,blank=True)
	marca   =models.CharField(max_length=30)
	zocalo  =models.CharField(max_length=20)	
	cant_BancosMemoria=models.IntegerField()
	cant_RanurasPci=models.IntegerField()
	precio  = models.DecimalField(max_digits=6,decimal_places=2)
	#componente=models.ForeignKey(Componente)

	def __unicode__(self):
		return self.nombre

class Carrito(models.Model):
	id_sesion=models.CharField(max_length=200)
	estado=models.BooleanField ( default = False )
	placa=models.IntegerField()
	cantidad=models.IntegerField()
