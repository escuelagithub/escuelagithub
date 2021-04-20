from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class disciplina(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre		
		
class curso(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField()
	disciplina = models.ForeignKey(disciplina,on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='core',blank=True,null=True)
	precio = models.DecimalField(decimal_places=2, default=0, max_digits=5)
	calificacion = models.DecimalField(decimal_places=1, default=0, max_digits=2)
	alumnos = models.IntegerField(default=0)
	profesor = models.ForeignKey(User,on_delete=models.CASCADE)
	completo = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.titulo

class inscripcion(models.Model):
	alumno = models.ForeignKey(User,on_delete=models.CASCADE)
	curso = models.ForeignKey(curso,on_delete=models.CASCADE)
	capitulo = models.IntegerField(default=1)
	tema = models.IntegerField(default=1)
	detalle = models.IntegerField(default=1)
	culminado = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.alumno + '-' + self.curso