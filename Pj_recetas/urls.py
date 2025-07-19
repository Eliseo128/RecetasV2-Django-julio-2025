from django.contrib import admin
from django.urls import path, include # Importar include
from django.conf import settings # Importar settings
from django.conf.urls.static import static # Importar static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirige cualquier petición a la app de recetas
    path('', include('app_receta.urls')),
]

# Añadir configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)