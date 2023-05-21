import datetime
from django import forms
from .models import Reserva
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

#VALIDACIONES EXTRAS
def validar_horario(value):
    hora = value.hour if isinstance(value, datetime.time) else value.hour
    if hora < 10 or hora > 22:
        raise forms.ValidationError("La hora debe estar entre 10 y 22.")



class ReservaForm(forms.ModelForm):
    
    fecha = forms.DateField(label='Fecha de reserva',widget=DatePickerInput(options={"format": "MM/DD/YYYY"}))
    hora = forms.TimeField(label='Hora de reserva',widget=TimePickerInput(options={"format": "HH"}),validators=[validar_horario])
    class Meta:
        model = Reserva
        exclude = ['id','mesa']

        
