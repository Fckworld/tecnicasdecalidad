from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'fecha', 'hora', 'nombre_cliente', 'email_cliente', 'telefono_cliente']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'datepicker'}),
            'hora': forms.TimeInput(attrs={'class': 'timepicker'}),
        }
