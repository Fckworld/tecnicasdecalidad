from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡El formulario se ha enviado exitosamente!')
                return redirect('contact')
            except IntegrityError:
                # Manejar la excepción de IntegrityError
                # Puede mostrar un mensaje de error al usuario o tomar alguna otra acción adecuada
                form.add_error(None, "Ocurrió un error al guardar los datos.")
    else:
        form = ContactForm()
    
    return render(request, "contact/contact.html",{'form':form})

    