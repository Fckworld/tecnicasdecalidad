from django.db import models
from datetime import datetime  
class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    
    def __str__(self):
        return f"Mesa {self.numero}"

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    
    def __str__(self):
        return f"Reserva para {self.nombre_cliente} en Mesa {self.mesa.numero}"
