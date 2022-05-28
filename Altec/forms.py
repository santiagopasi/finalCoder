from django import forms
from django.forms import ModelForm
from .models import *


class CrearPresupuestos(forms.Form):

    #Especificar los campos
    superficie = forms.FloatField()
    tipo_trabajo = forms.CharField()
    
class EditarEmpleados(ModelForm):
    class Meta:
        model = Empleados
        fields = "__all__"


