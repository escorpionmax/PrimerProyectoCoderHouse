from django.contrib import admin
from .models import Empleado, Impuestos
# Register your models here.
admin.site.register(Empleado)

admin.site.register(Impuestos)