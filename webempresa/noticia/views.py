from django.shortcuts import render, get_object_or_404
from .models import Noticia, Category

# Create your views here.

def noticia(request):
    noticias = Noticia.objects.all()
    
    return render(request, 'noticia/noticia.html', {'posts':noticias})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})