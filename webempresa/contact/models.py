from django.db import models
from datetime import datetime  
class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    contenido = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__(self):
        return f"Nombre contacto: {self.nombre}"
