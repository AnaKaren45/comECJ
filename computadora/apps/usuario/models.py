from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=60)
	
	def __unicode__(self):
		return self.nombre
class Componente(models.Model):
	categorias = models.ManyToManyField(Categoria,null=True,blank=True)
	nombre = models.CharField(max_length=60)
	modelo = models.CharField(max_length=60)
	marca = models.CharField(max_length=60)
	detalle = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	precio = models.DecimalField(max_digits=5,decimal_places=2)

	def __unicode__(self):
		return self.nombre