from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    fecha = forms.DateField()


class FormularioImpuestos(forms.Form):
    nombre_entidad = forms.CharField()
    nombre_concepto = forms.CharField()
    monto = forms.IntegerField()