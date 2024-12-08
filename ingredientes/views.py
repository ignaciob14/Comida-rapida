from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ComidaRapida

# Página principal
def mostrarIndex(request):
    return render(request, 'index.html')

# Listado de productos
def mostrarListado(request):
    productos = ComidaRapida.objects.all()
    return render(request, 'listado.html', {'productos': productos})

# Formulario de registro
def mostrarFormRegistrar(request):
    return render(request, 'registrar.html')

# Formulario de actualización
def mostrarFormActualizar(request, id):
    producto = get_object_or_404(ComidaRapida, id=id)
    return render(request, 'actualizar.html', {'producto': producto})

# Insertar un nuevo producto
def insertarProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        ingredientes = request.POST.get('ingredientes')
        tamanio = request.POST.get('tamanio')
        disponible = request.POST.get('disponible') == 'on'

        if not nombre or not categoria or not precio or not ingredientes or not tamanio:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('registrar')

        try:
            precio = float(precio)
        except ValueError:
            messages.error(request, 'El precio debe ser un número válido.')
            return redirect('registrar')

        ComidaRapida.objects.create(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            ingredientes=ingredientes,
            tamanio=tamanio,
            disponible=disponible
        )
        messages.success(request, 'Producto agregado exitosamente.')
        return redirect('listado')
    return redirect('registrar')

# Actualizar un producto existente
def actualizarProducto(request, id):
    producto = get_object_or_404(ComidaRapida, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.categoria = request.POST.get('categoria')
        producto.precio = request.POST.get('precio')
        producto.ingredientes = request.POST.get('ingredientes')
        producto.tamanio = request.POST.get('tamanio')
        producto.disponible = request.POST.get('disponible') == 'on'

        try:
            producto.precio = int(producto.precio)
        except ValueError:
            messages.error(request, 'El precio debe ser un número válido.')
            return redirect('actualizar', id=id)

        producto.save()
        messages.success(request, 'Producto actualizado exitosamente.')
        return redirect('listado')
    return redirect('actualizar', id=id)

# Eliminar un producto
def eliminarProducto(request, id):
    producto = get_object_or_404(ComidaRapida, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('listado')
