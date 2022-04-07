from django.db import models

# Create your models here.

class Impuestos(models.Model):
    entidad = models.CharField("Entidad", max_length=100)
    impuesto = models.CharField("Impuesto", max_length=100)
    observacion = models.CharField("Observación",max_length=100)
    n_comprobante = models.IntegerField("Numero comprobante")
    fecha = models.DateField("Fecha vencimiento", auto_now=False, auto_now_add=False)

    def __str__(self) :
        return f"{self.entidad} - {self.impuesto} - {self.observacion} - {self.n_comprobante} - {self.fecha}"
    
class Empleado(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField("Fecha Nacimiento", auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.dni} - {self.fecha_nacimiento}"

class Empresa(models.Model):
    representante = models.CharField("Representante", max_length=50)
    rubro = models.CharField("Rubro", max_length=50)
    domicilio = models.CharField("Domicilio", max_length=50)