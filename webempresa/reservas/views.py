from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservaForm

def reservas(request):

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡La reserva se ha registrado correctamente!')
                return redirect('reservas')
            except IntegrityError:
                # Manejar la excepción de IntegrityError
                # Puede mostrar un mensaje de error al usuario o tomar alguna otra acción adecuada
                form.add_error(None, "Ocurrió un error al guardar los datos.")
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/reservas.html', {'form': form})
