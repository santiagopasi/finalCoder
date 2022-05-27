from django.contrib import admin
from .models import Empleados,Presupuestos,TrabajosHechos

# Register your models here.
admin.site.register(Empleados)
admin.site.register(Presupuestos)
admin.site.register(TrabajosHechos)
