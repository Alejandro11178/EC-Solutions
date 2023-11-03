from django.db import models


# Create your models here.
class usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    correo= models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=50)
    es_profesor = models.BooleanField()
    materia = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=0)
