from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=60)
	
	def __unicode__(self):
		return self.nombre
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

class Componente(models.Model):
	def url(self,filename):
		ruta="MultimediaData/Componente/%s/%s"%(self.nombre,str(filename))
		return ruta
	Categoria   = models.ForeignKey(Categoria)	
	placa 		= models.ManyToManyField(Placa,null=True,blank=True)
	nombre     = models.CharField(max_length=60)
	imagen     = models.ImageField(upload_to=url,null=True,blank=True)
	modelo     = models.CharField(max_length=60)
	marca      = models.CharField(max_length=60)
	detalle    = models.CharField(max_length=100)
	cantidad   = models.IntegerField()
	precio     = models.DecimalField(max_digits=5,decimal_places=2)
	def __unicode__(self):
		return self.nombre


#class Compatibilidad(models.Model):
#	idPlaca=models.ForeignKey(Placa)
#	idComponente=models.ForeignKey(Componente)