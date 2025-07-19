# app_receta/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from django.contrib import messages

# Vista principal: Muestra, busca y crea recetas
def recetas(request):
    # Lógica para la búsqueda
    busqueda = request.GET.get("buscar")
    lista_recetas = Receta.objects.all().order_by('-id') # Ordena por más reciente

    if busqueda:
        lista_recetas = Receta.objects.filter(
            nombre_receta__icontains=busqueda
        ).distinct()

    # Lógica para crear una nueva receta (manejo del POST)
    if request.method == 'POST':
        nombre = request.POST.get("nombre_receta")
        descripcion = request.POST.get("descripcion_receta")
        imagen = request.FILES.get("imagen_receta")

        # Validación simple
        if not nombre or not descripcion:
            messages.error(request, "El nombre y la descripción son obligatorios.")
        else:
            # Crear y guardar la nueva receta
            Receta.objects.create(
                nombre_receta=nombre,
                descripcion_receta=descripcion,
                imagen_receta=imagen
            )
            messages.success(request, "Receta guardada exitosamente.")
            return redirect('recetas')

    return render(request, "receta.html", {"recetas": lista_recetas})


# Vista para actualizar una receta
def actualizar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':
        nombre = request.POST.get("nombre_receta")
        descripcion = request.POST.get("descripcion_receta")
        imagen = request.FILES.get("imagen_receta")

        receta.nombre_receta = nombre
        receta.descripcion_receta = descripcion
        
        # Solo actualiza la imagen si se sube una nueva
        if imagen:
            receta.imagen_receta = imagen
        
        receta.save()
        messages.success(request, "Receta actualizada correctamente.")
        return redirect('recetas')

    return render(request, "actualizar_receta.html", {"receta": receta})


# Vista para borrar una receta
def borrar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    messages.info(request, "La receta ha sido eliminada.")
    return redirect('recetas')