from django.shortcuts import render, redirect
from .forms import ReservaForm

def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/reservas.html', {'form': form})

def reserva_exitosa_view(request):
    return render(request, 'reserva_exitosa.html')