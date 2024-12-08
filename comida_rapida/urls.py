from django.contrib import admin
from django.urls import path
from ingredientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrarIndex, name='index'),
    path('listado/', views.mostrarListado, name='listado'),
    path('registrar/', views.mostrarFormRegistrar, name='registrar'),
    path('productos/registrar/', views.insertarProducto, name='productos_registrar'),
    path('insertar/', views.insertarProducto, name='insertar'),
    path('productos/', views.mostrarListado, name='productos'),  # Ruta para mostrar listado.
    path('actualizar/<int:id>/', views.mostrarFormActualizar, name='actualizar'),
    path('modificar/<int:id>/', views.actualizarProducto, name='modificar'),
    path('eliminar/<int:id>/', views.eliminarProducto, name='eliminar'),
]
