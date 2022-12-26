from django.db import models

class Carreras(models.Model):
    nombre = models.CharField(max_length=200)
    años = models.CharField(max_length=200)
    asignaturas = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
