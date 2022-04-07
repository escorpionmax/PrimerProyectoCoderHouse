from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_carga, name="Formulario"),
    path("busquedanombre/", views.buscar_datos, name="Buscarnombre"),
    path("buscar/", views.buscar, name="Buscar"),
    path('', views.inicio, name="Inicio"),
    path('mostrarEmpleados/',views.mostrar_empleados, name="MostrarEmpleados" ),
    path('eliminar/<id>/', views.eliminarEmpleado, name="Eliminar"),
    path('actualizar/<id>/', views.actualizar, name="Actualizar"),

    path('formularioi/', views.formmularioi, name="FormularioI"),
    path("busquedai/", views.buscar_datosi, name="BuscarnombreI"),
    path("buscari/", views.buscari, name="BuscarI"),
    path('mostrari/',views.mostrar_i, name="MostrarI" ),
    path('eliminari/<id>/', views.eliminari, name="EliminarI"),
    path('actualizari/<id>/', views.actualizari, name="ActualizarI"),
    
    path('formularioe/', views.formmularioe, name="FormularioE"),
    path("busquedae/", views.buscar_datose, name="BuscarnombreE"),
    path("buscare/", views.buscare, name="BuscarE"),
    path('mostrare/',views.mostrar_e, name="MostrarE" ),
    path('eliminare/<id>/', views.eliminare, name="EliminarE"),
    path('actualizare/<id>/', views.actualizare, name="ActualizarE"),


]

