import datetime
from django import forms
from django.core.validators import MaxValueValidator
from django.utils.timezone import now
from .models import Reserva
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

#VALIDACIONES EXTRAS
def validar_horario(value):
    
    hora_actual = now().time()
    print(hora_actual)
    hora = value.hour if isinstance(value, datetime.time) else value.hour
    if (hora < 10 or hora > 22):
        raise forms.ValidationError("El horario es entre 10:00 y 22:00 del dia")
    elif (value < hora_actual):
        raise forms.ValidationError("Debe ser antes de la hora actual")
        

def validar_fecha(value):
    fecha_actual = now().date()

    if value < fecha_actual and value != fecha_actual:
        raise forms.ValidationError("No se puede ingresar una fecha anterior.")
    elif (value.weekday() >= 5):  # 5 es sábado y 6 es domingo
        raise forms.ValidationError("No se puede seleccionar un sábado o domingo.")

class ReservaForm(forms.ModelForm):
    
    fecha = forms.DateField(label='Fecha de reserva',widget=DatePickerInput(options={"format": "DD/MM/YYYY"}),validators=[validar_fecha])
    hora = forms.TimeField(label='Hora de reserva',widget=TimePickerInput(options={"format": "HH:MM"}),validators=[validar_horario])
    cantidad_de_personas = forms.IntegerField(label='Cantidad de personas',validators=[MaxValueValidator(7)])
    class Meta:
        model = Reserva
        exclude = ['id','mesa']

        
