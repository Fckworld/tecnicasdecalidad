from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de services
    path('platillosemanal/', include('services.urls')),
    # Paths de blog
    # Paths de pages
    path('page/', include('pages.urls')),
    # Paths de pages
    path('contacto/', include('contact.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
    # Reservas
    path('reservas/', include('reservas.urls')),
    # Noticias
    path('noticia/', include('noticia.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
