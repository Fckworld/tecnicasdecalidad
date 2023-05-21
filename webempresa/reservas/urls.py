from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservas, name="reservas"),
    path('reserva_exitosa', views.reserva_exitosa, name="reserva_exitosa"),
]