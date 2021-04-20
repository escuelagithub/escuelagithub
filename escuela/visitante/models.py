from django.db import models

# Create your models here.
from core.models import curso

class alcance(models.Model):
	descripcion = models.TextField()
	curso = models.ForeignKey(curso, on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion

class recomendacion(models.Model):
	materia = models.TextField()
	nivel = models.CharField(max_length=10, default='m')
	curso = models.ForeignKey(curso, on_delete=models.CASCADE)

	def __str__(self):
		return self.materia

from ckeditor.fields import RichTextField

class capitulo(models.Model):
	nombre = models.TextField()
	descripcion = RichTextField()
	curso = models.ForeignKey(curso, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class tema(models.Model):
	nombre = models.TextField()
	descripcion = RichTextField()
	capitulo = models.ForeignKey(capitulo, on_delete=models.CASCADE)

def __str__(self):
	return self.nombre

class detalle(models.Model):
	nombre = models.TextField()
	descripcion = models.TextField(null=True,blank=True)
	imagen = models.ImageField(upload_to='core',blank=True,null=True)
	dirurl = models.URLField(max_length=200, blank=True)
	media = models.FileField(upload_to='visitante',null=True,blank=True)
	texto = RichTextField(null=True,blank=True)
	nombrearchivo = models.CharField(max_length=50, default='',null=True,blank=True)
	tipoarchivo = models.CharField(max_length=1, default='n')
	referencia_imagen = models.CharField(max_length=50, default='',null=True,blank=True)
	referencia_media = models.CharField(max_length=50, default='',null=True,blank=True)
	referencia_texto = models.CharField(max_length=50, default='',null=True,blank=True)
	tema = models.ForeignKey(tema, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

