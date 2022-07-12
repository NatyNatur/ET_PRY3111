from statistics import mode
from django.db import models

class Cliente(models.Model): 
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15, default='')
    direccion = models.CharField(max_length=100, default='')