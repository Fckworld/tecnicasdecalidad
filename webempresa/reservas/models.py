from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime  
class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    
    def __str__(self):
        return f"Mesa {self.numero}"

class Reserva(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE,null=True)
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_de_personas = models.IntegerField(max_length=10)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    
    def __str__(self):
        return f"Reserva del cliente: {self.nombre_cliente}"
    
    
