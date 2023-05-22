from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def menu(request):
    return render(request, "core/menu.html")

def informacion(request):
    return render(request, "core/informacion.html")