from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia, name="noticia"),
    path('category/<int:category_id>/', views.category, name="category"),
]