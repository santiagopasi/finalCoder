from django import forms


class CrearPresupuestos(forms.Form):

    #Especificar los campos
    superficie = forms.FloatField()
    tipo_trabajo = forms.CharField()


