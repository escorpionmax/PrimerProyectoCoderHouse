from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_carga, name="Formulario"),
    path("busquedanombre/", views.buscar_datos, name="Buscarnombre"),
    path("buscar/", views.buscar, name="Buscar"),
    path('actualizar/', views.actualizar, name="Actualizar"),
    path('', views.inicio, name="Inicio"),
    path('mostrarEmpleados/',views.mostrar_empleados, name="MostrarEmpleados" ),
    path('eliminar/<id>/', views.eliminarEmpleado, name="Eliminar"),
    path('actualizar/<id>/', views.actualizar, name="Actualizar"),
]

