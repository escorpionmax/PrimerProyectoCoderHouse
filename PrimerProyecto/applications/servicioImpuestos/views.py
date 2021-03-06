from django.shortcuts import render
from . import models
from . import forms


def inicio(request):
    return render(request, "index.html")

def formulario_carga(request):
    if request.method=="POST":
        formulario=forms.Formulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            empleado=models.Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], fecha_nacimiento=informacion['fecha'])
            empleado.save()
            return render(request,"creacion.html",  {"empleado":empleado})

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
        return render(request, "buscar.html")

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
            return render(request,"index.html",  {"nom":empleado.nombre, "apell":empleado.apellido})

    else:
        formulario = forms.Formulario(initial={"nombre":empleado.nombre, "apellido":empleado.apellido, "dni":empleado.dni, "fecha":empleado.fecha_nacimiento})

    return render(request, "actualizarEmpleado.html",{"miform":formulario, "nombre":empleado.nombre})

#-------------------------------Impuestos---------------------------------

def formmularioi(request):
    if request.method=="POST":
        formulario=forms.FormularioImpuestos(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            impuesto=models.Impuestos(entidad=informacion['entidad'], impuesto=informacion['impuesto'], observacion=informacion['observacion'], n_comprobante=informacion['n_comprobante'], fecha=informacion['fecha'])
            impuesto.save()
            return render(request,"creacioni.html",  {"impuesto":impuesto})

    else:
        formulario = forms.FormularioImpuestos()

    return render(request, "formularioi.html",{"miform":formulario})

def buscar_datosi(request):
    return render(request, "busquedanombrei.html")

def buscari(request): 

    if request.GET['entidad']:
        entidad=request.GET['entidad']
        impuestos=models.Impuestos.objects.filter(entidad=entidad)
        return render(request, "buscari.html", {"entidad":entidad, "impuestos":impuestos} )
    else:
        return render(request, "buscari.html")

def mostrar_i(request):
    impuestos=models.Impuestos.objects.all()
    return render(request, "mostrari.html", {"impuestos":impuestos})


def eliminari(request,id):
    impuesto=models.Impuestos.objects.get(id=id)
    impuesto.delete()
    impuestos=models.Impuestos.objects.all()
    return render(request, "mostrari.html",{"impuestos":impuestos})


def actualizari(request, id):
    impuesto=models.Impuestos.objects.get(id=id)

    if request.method=="POST":
        formulario=forms.FormularioImpuestos(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            impuesto.entidad=informacion['entidad']
            impuesto.impuesto=informacion['impuesto']
            impuesto.observacion=informacion['observacion']
            impuesto.n_comprobante=informacion['n_comprobante']
            impuesto.fecha=informacion['fecha']
            
            impuesto.save()
            return render(request,"index.html",  {"entidad":impuesto.entidad, "impuesto":impuesto.impuesto, "observacion":impuesto.observacion, "n_comprobante":impuesto.n_comprobante, "fecha":impuesto.fecha})

    else:
        formulario = forms.FormularioImpuestos(initial={"entidad":impuesto.entidad, "impuesto":impuesto.impuesto, "observacion":impuesto.observacion, "n_comprobante":impuesto.n_comprobante, "fecha":impuesto.fecha})

    return render(request, "actualizari.html",{"miform":formulario, "entidad":impuesto.entidad})



######################################Empresas################################

def formmularioe(request):
    if request.method=="POST":
        formulario=forms.FormularioEmpresa(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            empresa=models.Empresa(representante=informacion['representante'], rubro=informacion['rubro'], domicilio=informacion['domicilio'])
            empresa.save()
            return render(request,"creacione.html",  {"empresa":empresa})

    else:
        formulario = forms.FormularioEmpresa()

    return render(request, "formularioe.html",{"miform":formulario})

def buscar_datose(request):
    return render(request, "busquedanombree.html")

def buscare(request):

    if request.GET['rubro']:
        rubro=request.GET['rubro']
        empresas=models.Empresa.objects.filter(rubro=rubro)
        return render(request, "buscare.html", {"rubro":rubro, "empresas":empresas} )
    else:
        return render(request, "buscare.html")

def mostrar_e(request):
    empresas=models.Empresa.objects.all()
    return render(request, "mostrare.html", {"empresas":empresas})

def eliminare(request,id):
    empresa=models.Empresa.objects.get(id=id)
    empresa.delete()
    empresas=models.Empresa.objects.all()
    return render(request, "mostrare.html",{"empresas":empresas})

def actualizare(request, id):
    empresa=models.Empresa.objects.get(id=id)

    if request.method=="POST":
        formulario=forms.FormularioEmpresa(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            empresa.representante=informacion['representante']
            empresa.rubro=informacion['rubro']
            empresa.domicilio=informacion['domicilio']
            
            empresa.save()
            return render(request,"index.html",  {"representante":empresa.representante, "rubro":empresa.rubro, "domicilio":empresa.domicilio})

    else:
        formulario = forms.FormularioEmpresa(initial={"representante":empresa.representante, "rubro":empresa.rubro, "domicilio":empresa.domicilio})

    return render(request, "actualizare.html",{"miform":formulario, "representante":empresa.representante})