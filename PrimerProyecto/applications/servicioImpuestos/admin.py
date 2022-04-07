from django.contrib import admin
from .models import Empleado, Empresa, Impuestos
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Impuestos)
admin.site.register(Empresa)