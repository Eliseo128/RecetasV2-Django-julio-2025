# app_receta/models.py

from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    # Relación con el usuario que crea la receta (opcional)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_receta = models.CharField(max_length=100)
    descripcion_receta = models.TextField()
    # Campo para la imagen, se guardará en la carpeta 'media/recetas'
    imagen_receta = models.ImageField(upload_to="recetas", null=True, blank=True)
    # Contador simple de vistas (no implementado en las vistas, pero disponible)
    ver_contar_receta = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre_receta