from django.shortcuts import render
from . import models
from . import forms
from django.http import HttpResponse

def inicio(request):
    return render(request, "index.html")

def formulario_carga(request):
    if request.method=="POST":
        formulario=forms.Formulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            empleado=models.Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], fecha_nacimiento=informacion['fecha'])
            empleado.save()
            return render(request,"creacion.html",  {"nom":empleado.nombre, "apell":empleado.apellido})

    else:
        formulario = forms.Formulario()

    return render(request, "formulario.html",{"miform":formulario})



def buscar_datos(request):
    return render(request, "busquedanombre.html")

def buscar(request):

    if request.GET['apellido']:
        apellidos=request.GET['apellido']
        empleados=models.Empleado.objects.filter(apellido=apellidos)
        return render(request, "buscar.html", {"apellido":apellidos, "emp":empleados} )
    else:
        return HttpResponse("No enviaste un apellido para buscar")
        

def mostrar_empleados(request):
    empleados=models.Empleado.objects.all()
    return render(request, "mostrarEmpleados.html", {"emp":empleados})


def eliminarEmpleado(request,id):
    empleado=models.Empleado.objects.get(id=id)
    empleado.delete()
    empleados=models.Empleado.objects.all()
    return render(request, "mostrarEmpleados.html",{"emp":empleados})

def actualizar(request, id):
    empleado=models.Empleado.objects.get(id=id)

    if request.method=="POST":
        formulario=forms.Formulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            empleado.nombre=informacion['nombre']
            empleado.apellido=informacion['apellido']
            empleado.dni=informacion['dni']
            empleado.fecha_nacimiento=informacion['fecha']
            
            empleado.save()
            return render(request,"formulario.html",  {"nom":empleado.nombre, "apell":empleado.apellido})

    else:
        formulario = forms.Formulario(initial={"nombre":empleado.nombre, "apellido":empleado.apellido, "dni":empleado.dni, "fecha":empleado.fecha_nacimiento})

    return render(request, "actualizarEmpleado.html",{"miform":formulario, "nombre":empleado.nombre})
