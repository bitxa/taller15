"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listado_edificios/<int:id>', views.obtener_edificios, name= 'listado_edificios'),
    path('listado_departamentos/<int:id>', views.obtener_departamentos, name= 'listado_departamento'),
    path('listado_propietarios/<int:id>', views.obtener_propietarios, name= 'listado_propietario'),
    
    path('crear/edificio', views.crear_edificio, name = 'crear_edificio'),
    path('crear/departameto', views.crear_departamento, name = 'crear_departamento'),
    path('crear/propietario', views.crear_propietario, name = 'crear_propietario'),
    
    path('editar_edificio/<int:id>', views.editar_edificio, name = 'editar_edificio'),
    path('editar_departamento/<int:id>', views.editar_departamento, name = 'editar_departamento'),
    path('editar_propietario/<int:id>', views.editar_propietario, name = 'editar_propietario'),
    
    path('eliminar_edificio/<int:id>', views.eliminar_edificio, name = 'eliminar_edificio'),
    path('eliminar_departamento/<int:id>', views.eliminar_departamento, name = 'eliminar_departamento'),
    path('eliminar_propietario/<int:id>', views.eliminar_propietario, name = 'eliminar_propietario'),
]