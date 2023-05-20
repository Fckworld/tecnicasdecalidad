from django.contrib import admin
from .models import Mesa, Reserva

# Register your models here.
class MesaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('mesa', 'nombre_cliente', 'email_cliente', 'telefono_cliente')
    ordering = ('nombre_cliente', 'created')
    search_fields = ('mesa__numero','nombre_cliente','email_cliente', 'categories__name')



admin.site.register(Mesa, MesaAdmin)
admin.site.register(Reserva, ReservaAdmin)