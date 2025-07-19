# app_receta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL principal que muestra el formulario y la lista de recetas
    path('', views.recetas, name='recetas'),
    # URL para borrar una receta específica por su ID
    path('borrar_receta/<int:id>', views.borrar_receta, name='borrar_receta'),
    # URL para la página de actualización de una receta
    path('actualizar_receta/<int:id>', views.actualizar_receta, name='actualizar_receta'),
]