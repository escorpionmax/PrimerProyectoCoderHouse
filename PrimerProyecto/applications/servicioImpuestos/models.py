from django.db import models

# Create your models here.

class Impuestos(models.Model):
    nombre_entidad = models.CharField("Nombre Entidad", max_length=100)
    nombre_concepto = models.CharField("Nombre Concepto", max_length=100)
    monto = models.IntegerField()
     
    def __str__(self) :
        return f"{self.nombre_concepto} - {self.nombre_concepto} - {self.monto}"
    
class Empleado(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField("Fecha Nacimiento", auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.nombre}"


