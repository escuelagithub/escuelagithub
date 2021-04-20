from django.db import models

from django.db import models
from django.contrib.auth.models import User

class perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, default='', blank=False)
	avatar = models.ImageField(upload_to='perfiles',null=True,blank=True)
	biografia = models.TextField(null=True,blank=True)
	recibemails = models.BooleanField(default=False)
	visitante = models.BooleanField(default=True)
	alumno = models.BooleanField(default=False)
	profesor = models.BooleanField(default=False)
	sexo = models.CharField(max_length=1,default='F')
	nacimiento = models.DateField(blank=True,null=True)
