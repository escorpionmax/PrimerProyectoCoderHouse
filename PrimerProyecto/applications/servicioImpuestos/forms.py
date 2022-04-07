
from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    fecha = forms.DateField()

class FormularioImpuestos(forms.Form):
    entidad = forms.CharField()
    impuesto = forms.CharField()
    observacion = forms.CharField()
    n_comprobante = forms.IntegerField()
    fecha = forms.DateField()

class FormularioEmpresa(forms.Form):
    representante = forms.CharField()
    rubro = forms.CharField()
    domicilio = forms.CharField()