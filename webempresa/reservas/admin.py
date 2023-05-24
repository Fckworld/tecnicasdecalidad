from django.contrib import admin
from .models import Mesa, Reserva

# Register your models here.
class MesaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('numero','capacidad','disponible')
class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('fecha','hora','mesa', 'nombre_cliente', 'email_cliente', 'telefono_cliente')
    ordering = ('fecha', 'created')
    search_fields = ('mesa__numero','nombre_cliente','email_cliente', 'categories__name')



admin.site.register(Mesa, MesaAdmin)
admin.site.register(Reserva, ReservaAdmin)